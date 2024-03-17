class OrderNotFulfilledError(Exception):
    """Raised when order is not executed"""

    def __init__(self, action: str, symbol: str, price: float, action_type: str):
        super().__init__(
            f"Order not fullfilled execution price {price} on stock {symbol}. Action = {action} and Type = {action_type}"
        )
        self.action = action
        self.symbol = symbol
        self.price = price
        self.action_type = action_type


class LoginError(Exception):
    """Raised when login is not possible"""

    def __init__(self, account: str, error):
        super().__init__(
            f"failed to connect to trade account {account} error code = {error}"
        )
        self.account = account
