from products.models import SpotAssetProduct, SpotAssetPrice
from datetime import datetime
import yfinance as yf

TICKER_MAP = {
    "gold": "GLD",
    "silver": "SLV",
    "oil": "USO",
    "gas": "UNG",
    "corn": "CORN",
    "wheat": "WEAT",
    "soybean": "SOYB",
    "copper": "CPER",
    "platinum": "PPLT",
    "palladium": "PALL",
}


def save_asset_prices(name, start="2020-01-01", end=None):
    if name not in TICKER_MAP:
        raise ValueError(f"{name}은(는) 지원하지 않는 원자재입니다.")

    if end is None:
        end = datetime.today().strftime("%Y-%m-%d")

    print(f"{name} 데이터 api 요청 시작")
    # 1. SpotAssetProduct 가져오기 (없으면 생성)
    product, _ = SpotAssetProduct.objects.get_or_create(name=name)

    # 2. yfinance 데이터 받아오기
    ticker = yf.Ticker(TICKER_MAP[name])
    hist = ticker.history(start=start, end=end)

    # 3. 가격 저장
    count = 0
    for idx, row in hist.iterrows():
        date = idx.date()
        price = row["Close"]
        if (
            price
            and not SpotAssetPrice.objects.filter(product=product, date=date).exists()
        ):
            SpotAssetPrice.objects.create(product=product, date=date, close_price=price)
            count += 1

    return count
