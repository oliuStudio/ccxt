from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_info_status = publicGetInfoStatus = Entry('info/status', 'public', 'GET', {'cost': 1})
    public_get_info_markets = publicGetInfoMarkets = Entry('info/markets', 'public', 'GET', {'cost': 1})
    public_get_info_ticker = publicGetInfoTicker = Entry('info/ticker', 'public', 'GET', {'cost': 1})
    public_get_info_orderbook = publicGetInfoOrderbook = Entry('info/orderbook', 'public', 'GET', {'cost': 1})
    public_get_info_trades = publicGetInfoTrades = Entry('info/trades', 'public', 'GET', {'cost': 1})
    public_get_candlestick_candlesticks = publicGetCandlestickCandlesticks = Entry('candlestick/candlesticks', 'public', 'GET', {'cost': 1})
    
    private_get_account_account = privateGetAccountAccount = Entry('account/account', 'private', 'GET', {'cost': 1})
    private_get_account_positions = privateGetAccountPositions = Entry('account/positions', 'private', 'GET', {'cost': 1})
    private_get_account_orders = privateGetAccountOrders = Entry('account/orders', 'private', 'GET', {'cost': 1})
    private_get_account_trades = privateGetAccountTrades = Entry('account/trades', 'private', 'GET', {'cost': 1})
    
    private_post_order_create = privatePostOrderCreate = Entry('order/create', 'private', 'POST', {'cost': 1})
    private_post_order_cancel = privatePostOrderCancel = Entry('order/cancel', 'private', 'POST', {'cost': 1})
    private_post_order_cancel_all = privatePostOrderCancelAll = Entry('order/cancel-all', 'private', 'POST', {'cost': 1})
