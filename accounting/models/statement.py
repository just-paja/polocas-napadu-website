from django.dispatch import Signal
from django.db.models import (
    CASCADE,
    DateTimeField,
    ForeignKey,
    CharField,
    PROTECT,
    TextField,
)
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from .counter_party import KnownAccount
from .promise import Promise
from .statement_specs import StatementSpecification, StatementSenderSpecification


statement_registered = Signal(providing_args=['instance'])


class Statement(
    StatementSenderSpecification,
    StatementSpecification,
    TimeStampedModel
):

    class Meta:
        verbose_name = _('Statement')
        verbose_name_plural = _('Statements')

    account = ForeignKey(
        'Account',
        blank=False,
        null=False,
        on_delete=CASCADE,
        related_name='statements',
    )
    promise = ForeignKey(
        'Promise',
        blank=True,
        null=True,
        on_delete=CASCADE,
        related_name='statements',
    )
    counterparty = ForeignKey(
        'CounterParty',
        blank=True,
        null=True,
        on_delete=PROTECT,
        related_name='statements',
    )
    ident = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Payment identificator"),
        help_text=_("Payment identificator, usually generated by the bank"),
    )
    received_at = DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Date Time received"),
        help_text=_("When was the payment received by our bank"),
    )
    user_identification = CharField(
        verbose_name=_("User identification"),
        help_text=_("User identification given by the bank"),
        max_length=255,
        null=True,
        blank=True,
    )
    message = TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Message"),
    )
    scrape = ForeignKey(
        'BankScrape',
        blank=True,
        null=True,
        on_delete=CASCADE,
        related_name='statements',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_promise = self.promise

    def __str__(self):
        return 'Statement#%s' % self.id

    def save(self, *args, **kwargs):
        self.pair_with_known_accounts()
        self.pair_with_promises()
        super().save(*args, **kwargs)
        self.update_promises()
        statement_registered.send(sender=self.__class__, instance=self)

    def pair_with_promises(self):
        if not self.promise and self.variable_symbol:
            self.promise = Promise.objects.filter_by_transaction(
                self.variable_symbol,
                self.specific_symbol,
            ).first()

    def pair_with_known_accounts(self):
        if not self.counterparty:
            known_account = None
            if self.sender_account_number and self.sender_bank:
                known_account = KnownAccount.objects.filter(
                    sender_account_number=self.sender_account_number,
                    sender_bank=self.sender_bank,
                ).first()
            elif self.sender_iban:
                known_account = KnownAccount.objects.filter(
                    sender_iban=self.sender_iban,
                ).first()
            self.counterparty = known_account.owner if known_account else None

    def update_promises(self):
        if self.promise:
            self.promise.save()
