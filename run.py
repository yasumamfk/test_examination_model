from bq.reader.bq_reader import BQReader
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='run.py',
        usage='',
        description='description',
        epilog='end',
        add_help=True,
    )
    parser.add_argument('-p', '--project')

    # 引数を解析する
    args = parser.parse_args()
    PROJECT_ID = args.project
    if PROJECT_ID in ['mfk-dev']:
        bqr = BQReader(PROJECT_ID)
        bqr.output()
