#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Self-health check pro Hermes agenta.
Kontroluje: gateway instance, telegram, cron, syncthing, weby.
Vrací JSON výsledek — pro cron delivery do Telegramu.
"""
import json, subprocess, os, sys, socket
from datetime import datetime

def check():
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    issues = []
    ok = []

    # 1) GATEWAY — právě 1 instance
    try:
        r = subprocess.run(["powershell", "-Command",
            "Get-CimInstance Win32_Process | Where-Object {$_.CommandLine -match 'gateway run'} | Measure-Object | Select-Object -ExpandProperty Count"],
            capture_output=True, text=True, timeout=15)
        gw_count = int(r.stdout.strip() or 0)
        if gw_count == 1:
            ok.append("✅ Gateway: 1 instance")
        elif gw_count == 0:
            issues.append("❌ Gateway: NENÍ SPUŠTĚN!")
        else:
            issues.append(f"⚠️ Gateway: {gw_count} instancí (měla být 1)")
    except Exception as e:
        issues.append(f"⚠️ Gateway check selhal: {e}")

    # 2) TELEGRAM BOT — odpovídá na getMe
    try:
        import urllib.request
        # token z env
        env_path = r"C:\Users\vacla\AppData\Local\hermes\.env"
        token = None
        with open(env_path, encoding='utf-8') as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    token = line.split("=",1)[1].strip()
                    break
        if token:
            req = urllib.request.Request(f"https://api.telegram.org/bot{token}/getMe")
            resp = json.load(urllib.request.urlopen(req, timeout=10))
            if resp.get("ok"):
                ok.append(f"✅ Telegram: bot @{resp['result']['username']} online")
            else:
                issues.append("❌ Telegram: bot neodpovídá")
        else:
            issues.append("⚠️ Telegram: token nenalezen")
    except Exception as e:
        issues.append(f"❌ Telegram: {e}")

    # 3) CRON JOBS — běží?
    try:
        r = subprocess.run(["hermes", "cron", "list"], capture_output=True, text=True, timeout=20)
        if "active" in r.stdout:
            # počet active
            active = r.stdout.count("[active]")
            ok.append(f"✅ Cron: {active} aktivních jobů")
        else:
            issues.append("⚠️ Cron: žádné aktivní joby")
    except Exception as e:
        issues.append(f"⚠️ Cron check selhal: {e}")

    # 4) SYNCTHING — běží a nedělá smazání ve Wendy
    try:
        r = subprocess.run(["powershell", "-Command",
            "Get-Process syncthing -ErrorAction SilentlyContinue | Measure-Object | Select-Object -ExpandProperty Count"],
            capture_output=True, text=True, timeout=10)
        st_count = int(r.stdout.strip() or 0)
        if st_count >= 1:
            ok.append(f"✅ Syncthing: {st_count} procesů")
        else:
            issues.append("⚠️ Syncthing: neběží")
    except Exception as e:
        issues.append(f"⚠️ Syncthing check: {e}")

    # 5) WEBY — dostupnost polarita.cz a polarita.eu
    for url in ["https://www.polarita.cz", "https://www.polarita.eu"]:
        try:
            import urllib.request
            req = urllib.request.Request(url, method="HEAD")
            req.add_header("User-Agent", "Mozilla/5.0")
            resp = urllib.request.urlopen(req, timeout=10)
            if resp.status == 200:
                ok.append(f"✅ Web {url.split('//')[1]}: online")
            else:
                issues.append(f"⚠️ Web {url.split('//')[1]}: HTTP {resp.status}")
        except Exception as e:
            issues.append(f"❌ Web {url.split('//')[1]}: OFFLINE ({e})")

    # 6) DISK — volné místo na D:
    try:
        r = subprocess.run(["powershell", "-Command",
            "Get-PSDrive D | Select-Object -ExpandProperty Free"],
            capture_output=True, text=True, timeout=10)
        free_gb = int(r.stdout.strip()) / (1024**3)
        if free_gb > 5:
            ok.append(f"✅ Disk D: {free_gb:.1f} GB volné")
        else:
            issues.append(f"⚠️ Disk D: jen {free_gb:.1f} GB volné!")
    except Exception as e:
        issues.append(f"⚠️ Disk check: {e}")

    # Výsledek
    result = {
        "timestamp": now,
        "status": "HEALTHY" if not issues else "DEGRADED" if len(issues) < 3 else "CRITICAL",
        "ok": ok,
        "issues": issues
    }
    return result

if __name__ == "__main__":
    r = check()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    # exit code 0 = OK, 1 = issues
    sys.exit(1 if r["issues"] else 0)
