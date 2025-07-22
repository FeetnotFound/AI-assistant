#This file is for when your gpu runs out of memory space.
#This will stop any python processes that are using your vram

import gpustat
import subprocess

def get_gpu_processes_gpustat():
    try:
        gpu_stats = gpustat.new_query()
        gpu_processes = []
        for gpu in gpu_stats:
            for process in gpu.processes:
                gpu_processes.append({
                    "pid": process["pid"],
                    "name": process["command"],
                    "gpu_memory_usage": process["gpu_memory_usage"]
                })
        return gpu_processes
    except Exception as e:
        print(f"Error using gpustat: {e}")
        return []

if __name__ == "__main__":
    processes = get_gpu_processes_gpustat()
    if processes:
        for process in processes:
            print(f"PID: {process['pid']},Name: {process['name']}, Memory Usage: {process['gpu_memory_usage']}")
            if process['name'] == "python":
                result = subprocess.run(['bash', '-c', f"sudo kill -9 {process['pid']}"], capture_output=True, text=True)
                print(result)
            else:
                continue
    else:
        print("No GPU processes found.")