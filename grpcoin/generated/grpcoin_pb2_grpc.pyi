"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import grpcoin_pb2
import typing

class TickerInfoStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Watch: grpc.UnaryStreamMultiCallable[
        grpcoin_pb2.TickerWatchRequest,
        grpcoin_pb2.Quote] = ...
    """Watch returns real-time quotes of the ticker.
    The only supported tickers are "BTC", "ETH", "DOGE", "DOT".

    This stream terminates after 15 minutes, so expect being
    abruptly disconnected and need to reconnect.

    No authentication required.
    """


class TickerInfoServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Watch(self,
        request: grpcoin_pb2.TickerWatchRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[grpcoin_pb2.Quote]:
        """Watch returns real-time quotes of the ticker.
        The only supported tickers are "BTC", "ETH", "DOGE", "DOT".

        This stream terminates after 15 minutes, so expect being
        abruptly disconnected and need to reconnect.

        No authentication required.
        """
        pass


def add_TickerInfoServicer_to_server(servicer: TickerInfoServicer, server: grpc.Server) -> None: ...

class PaperTradeStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Portfolio: grpc.UnaryUnaryMultiCallable[
        grpcoin_pb2.PortfolioRequest,
        grpcoin_pb2.PortfolioResponse] = ...
    """Returns authenticated user's portfolio."""

    Trade: grpc.UnaryUnaryMultiCallable[
        grpcoin_pb2.TradeRequest,
        grpcoin_pb2.TradeResponse] = ...
    """Executes a trade in authenticated user's portfolio.
    All trades are executed immediately with the real-time market
    price provided on TickerInfo.Watch endpoint.
    """

    ListSupportedCurrencies: grpc.UnaryUnaryMultiCallable[
        grpcoin_pb2.ListSupportedCurrenciesRequest,
        grpcoin_pb2.ListSupportedCurrenciesResponse] = ...
    """Returns symbols supported by Trade or Watch methods."""


class PaperTradeServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Portfolio(self,
        request: grpcoin_pb2.PortfolioRequest,
        context: grpc.ServicerContext,
    ) -> grpcoin_pb2.PortfolioResponse:
        """Returns authenticated user's portfolio."""
        pass

    @abc.abstractmethod
    def Trade(self,
        request: grpcoin_pb2.TradeRequest,
        context: grpc.ServicerContext,
    ) -> grpcoin_pb2.TradeResponse:
        """Executes a trade in authenticated user's portfolio.
        All trades are executed immediately with the real-time market
        price provided on TickerInfo.Watch endpoint.
        """
        pass

    @abc.abstractmethod
    def ListSupportedCurrencies(self,
        request: grpcoin_pb2.ListSupportedCurrenciesRequest,
        context: grpc.ServicerContext,
    ) -> grpcoin_pb2.ListSupportedCurrenciesResponse:
        """Returns symbols supported by Trade or Watch methods."""
        pass


def add_PaperTradeServicer_to_server(servicer: PaperTradeServicer, server: grpc.Server) -> None: ...

class AccountStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    TestAuth: grpc.UnaryUnaryMultiCallable[
        grpcoin_pb2.TestAuthRequest,
        grpcoin_pb2.TestAuthResponse] = ...
    """Tests if your token works.

    Send a header (gRPC metadata) named "Authorization"
    with value "Bearer XXX" where XXX is a GitHub Personal Access token
    from https://github.com/settings/tokens (no permissions needed).
    """


class AccountServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def TestAuth(self,
        request: grpcoin_pb2.TestAuthRequest,
        context: grpc.ServicerContext,
    ) -> grpcoin_pb2.TestAuthResponse:
        """Tests if your token works.

        Send a header (gRPC metadata) named "Authorization"
        with value "Bearer XXX" where XXX is a GitHub Personal Access token
        from https://github.com/settings/tokens (no permissions needed).
        """
        pass


def add_AccountServicer_to_server(servicer: AccountServicer, server: grpc.Server) -> None: ...
