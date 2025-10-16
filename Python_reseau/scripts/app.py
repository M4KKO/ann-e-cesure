from flask import Flask, request
import socket
import ipaddress

def scan_port(ip: str, port: int, timeout: float = 2.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        return {"port": port, "etat": "ouvert", "msg": "connexion réussie, le port est ouvert"}
    except ConnectionRefusedError:
        return {"port": port, "etat": "fermer", "msg": "port fermé (connexion refusée)"}
    except socket.timeout:
        return {"port": port, "etat": "fermer", "msg": "timeout (pas de réponse)"}
    except Exception as e:
        return {"port": port, "etat": "fermer", "msg": f"erreur inattendue: {e}"}
    finally:
        try:
            s.close()
        except Exception:
            pass

def is_valid_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
app = Flask(__name__)  # crée l'application

@app.route("/")
def home():
    return "Scanner en ligne ✅"

@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        ip = request.form.get("ip", "").strip()
        port_str = request.form.get("port", "").strip()

        if not ip or not port_str:
            return "IP et port requis", 400
        if not is_valid_ip(ip):
            return "Adresse IP invalide", 400

# préparer la liste des ports
        ports = []
        for p in port_str.split(","):
            p = p.strip()
            if not p:
                continue
            try:
                port_num = int(p)
            except ValueError:
                return f"Port invalide : {p} (doit être un nombre)", 400
            if not (1 <= port_num <= 65535):
                return f"Port hors plage : {p}", 400
            ports.append(port_num)

# construire les lignes
        rows = ""
        resultats=[]
        for port in ports:
            result = scan_port(ip, port)
            resultats.append(result)
            if result["etat"]=="ouvert": 
                couleur = "green"
            else :
                couleur="red"

            rows += f"""
              <tr>
                <td>{result['port']}</td>
                <td style="color:{couleur}; font-weight:bold">{result['etat']}</td>
                <td>{result['msg']}</td>
              </tr>
            """
        nbr_ports=len(resultats)
        compteur_port_ouvert = sum(1 for r in resultats if r["etat"] == "ouvert")
        compteur_port_ferme=nbr_ports-compteur_port_ouvert
   # assembler la table complète
        html = f"""
        <h2>Résultats pour {ip}</h2>
        <table border="1" cellpadding="6" cellspacing="0">
          <tr><th>Port</th><th>État</th><th>Message</th></tr>
          {rows}
        </table>
        <p>Ports testés : {nbr_ports} — ouverts : {compteur_port_ouvert} — fermés : {compteur_port_ferme}</p>
        <p><a href="/scan">← Nouveau scan</a></p>
        """

        return html

    # en GET : formulaire simple
    return """
        <form method="post">
            IP : <input type="text" name="ip"><br>
            Port : <input type="text" name="port"><br>
            <button type="submit">Scanner</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=False)  # lance le serveur en local (http://127.0.0.1:5000)
