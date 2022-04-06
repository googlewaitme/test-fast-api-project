from environs import Env


env = Env()
env.read_env()

PROJECT_ID = env.str('PROJECT_ID')
PROJECT_SECRET = env.str('PROJECT_SECRET')
PROJECT_RINKEBY_ENDPOINT = env.str('PROJECT_RINKEBY_ENDPOINT')

CONTRACT_ADDRESS = env.str('CONTRACT_ADDRESS')
PATH_TO_ABI_FILE = env.str("PATH_TO_ABI_FILE")

PRIVATE_KEY = env.str('PRIVATE_KEY')

with open(PATH_TO_ABI_FILE, 'r') as file_input:
    CONTRACT_ABI = file_input.readline()
