import argparse
from client import BinanceClient
from validators import validate_input
from logging_config import setup_logger

logger = setup_logger()

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.qty, args.price)

        bot = BinanceClient(API_KEY, API_SECRET)

        logger.info("Placing order request")

        order = bot.place_order(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price
        )

        print("\nORDER SUCCESSFUL")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print(order)

        logger.info(order)

    except Exception as e:
        print("ERROR:", str(e))
        logger.error(str(e))

if __name__ == "__main__":
    main()
