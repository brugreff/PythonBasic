# Módulo time - funções relacionadas a tempo

# Exemplo - chamada das funções time() e ctime()
# time(): nº de seg passados desde o início da contagem (padrão de início 00:00:00 de 1 de jan de 1970)
# ctime(): string representando horário local, calc. a partir do nº de seg. passado como parâmetro

import time

x = time.time()
print(f'Local time: {time.ctime(x)}')

# Variável x recebe nº de seg. desde 00:00:00 de 01/01/1970 pela função time()
# Na execução de ctime(), o nº de seg. armazenado em x é convertido em uma string com o horário local
