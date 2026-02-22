# 🛡️ Cybersecurity Labs & Troubleshooting
Laboratórios de Pentest, Hardening de sistemas e automação de segurança.

## 🐍 1. Network Port Scanner (Python)
Script desenvolvido em Python para validação de serviços ativos. Este projeto une conceitos de **ADS** com Cybersecurity.
* **Arquivo:** `port_scanner.py`
* **Status:** Concluído. Identifica portas críticas como 22 (SSH) e 80 (HTTP).

## 🧱 2. Defesa com Firewall (Blue Team)
Configuração de regras de proteção para mitigar superfícies de ataque.
* **Ferramenta:** UFW (Uncomplicated Firewall).
* **Ação:** Bloqueio da porta 80/TCP.
* **Comando:** `sudo ufw deny 80/tcp`.

## 🔎 3. Auditoria de Vulnerabilidades (Nikto)
Análise detalhada do servidor Apache para encontrar falhas de configuração.
* **Principais achados:**
    * Vulnerabilidade a Clickjacking (falta de X-Frame-Options).
    * Exposição do diretório `/server-status`.
    * Vazamento de informações via ETags.
