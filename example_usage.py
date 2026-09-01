from client import IsolatedEphemeralCodeExecutionSandboxClient

def main():
    client = IsolatedEphemeralCodeExecutionSandboxClient()
    res = client.execute_in_isolated_microvm('PYTHON_3_13', 'print("Sandbox execution active")')
    print('Ephemeral Code Sandbox: ' + res['sandbox_execution_id'] + ' (' + res['runtime_language'] + ')')
    print('Boot Latency: ' + str(res['microvm_boot_latency_ms']) + 'ms | Exit Code: ' + str(res['exit_code']))
    print('Output: ' + res['stdout_captured'])

if __name__ == '__main__':
    main()
