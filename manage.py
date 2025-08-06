"""Command line interface for the dashboard prototype."""

from __future__ import annotations

import argparse


def init_db() -> None:
    """Initialize database (placeholder)."""
    print("init-db executed")


def run_etl(adm: str, start: str, end: str) -> None:
    """Run ETL for given administrator (placeholder)."""
    print(f"etl for {adm} from {start} to {end}")


def run_server(reload: bool) -> None:
    """Run development server (placeholder)."""
    flag = " with reload" if reload else ""
    print(f"run server{flag}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage dashboard tasks")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init-db")

    etl_p = sub.add_parser("etl")
    etl_p.add_argument("--adm", required=True)
    etl_p.add_argument("--start", required=True)
    etl_p.add_argument("--end", required=True)

    run_p = sub.add_parser("run")
    run_p.add_argument("--reload", action="store_true")

    args = parser.parse_args()
    if args.command == "init-db":
        init_db()
    elif args.command == "etl":
        run_etl(args.adm, args.start, args.end)
    elif args.command == "run":
        run_server(args.reload)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
