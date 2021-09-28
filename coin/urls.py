from django.urls import path

from coin.views.buys import UserBuysView, UserBuyOrderView
from coin.views.currency import ListCurrencyDetails
from coin.views.payment_methods import ListPaymentMethodsView, PaymentMethodsView
from coin.views.prices import UserBuyPrice, UserSellPrice, UserSpotPrice
from coin.views.sells import ListsSellsView, UserSellView
from coin.views.transactions import ListTransactionView, TransactionDetailsView
from coin.views.user import CurrentUserDetailsView, UserDetailsView, UserAuthView
from coin.views.accounts import AccountsDetailsView, AccountDetailsView
from coin.views.exchange_rates import ExchangeRatesDetails

app_name = "coin"

PATTERNS = (
    [
        path(
            "current-user",
            CurrentUserDetailsView.as_view(),
            name="current-user-details",
        ),
        path(
            "<user_id>/user",
            UserDetailsView.as_view(),
            name="user-details",
        ),
        path(
            "user-auth",
            UserAuthView.as_view(),
            name="user-auth",
        ),

        path(
            "user-accounts",
            AccountsDetailsView.as_view(),
            name="user-accounts",
        ),
        path(
            "<account_id>/user-account",
            AccountDetailsView.as_view(),
            name="user-specific-account",
        ),
        path(
            "<account_id>/user-account-transactions",
            ListTransactionView.as_view(),
            name="user-account-transactions"
        ),
        path(
            "<account_id>/user-account-transaction/<transaction_id>",
            TransactionDetailsView.as_view(),
            name="user-account-transaction"
        ),
        path(
            "<account_id>/user-buys",
            UserBuysView.as_view(),
            name="user-buys"
        ),
        path(
            "<account_id>/user-buys/<buy_id>",
            UserBuyOrderView.as_view(),
            name="user-buys-orders"
        ),
        path(
            "user-payment-methods",
            ListPaymentMethodsView.as_view(),
            name="user-payment-methods"
        ),
        path(
            "user-payment-methods/<payment_id>",
            PaymentMethodsView.as_view(),
            name="user-payment-method"
        ),
        path(
            "<account_id>/user-sells",
            ListsSellsView.as_view(),
            name="user-sells"
        ),
        path(
            "<account_id>/user-sell/<sell_id>",
            UserSellView.as_view(),
            name="user-sell"
        ),
        path(
            "user-currency",
            ListCurrencyDetails.as_view(),
            name="user-currency-list"
        ),

        path(
            "user-exchange-rates",
            ExchangeRatesDetails.as_view(),
            name="user-exchange-rates"
        ),
        path(
            "user-buy-price",
            UserBuyPrice.as_view(),
            name="user-buy-price"
        ),
        path(
            "user-sell-price",
            UserSellPrice.as_view(),
            name="user-sell-price"
        ),
        path(
            "user-spot-price",
            UserSpotPrice.as_view(),
            name="user-spot-price"
        ),

    ]
)
