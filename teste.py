import psutil
import time

# Nome do processo que você está procurando
target_process_name = "Abacos.exe"

while True:
    # Iterar por todos os processos em execução
    for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
        if process.info['name'] == target_process_name:
            print(f"Processo {target_process_name} encontrado com PID {process.info['pid']}")
            print(f"Status: {process.info['status']}")
            break  # Se você encontrou o processo, você pode parar de procurar

    # Se o processo não for encontrado
    else:
        print(f"Processo {target_process_name} não encontrado.")

    # Aguarde 1 segundo antes de verificar novamente
    time.sleep(1)
