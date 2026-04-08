from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Funzione per connettersi al database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def dashboard():
    # Simuliamo alcuni dati per la dashboard (in futuro verranno dal DB)
    dati_riepilogo = {
        "pratiche_urgenti": 3,
        "morosita_totale": "4.500",
        "assemblee_imminenti": 2
    }
    
    scadenze = [
        {"titolo": "Revisione Ascensore", "condominio": "Condominio Roma", "giorni": 3, "stato": "in-arrivo"},
        {"titolo": "Rata Assicurazione", "condominio": "Condominio Milano", "giorni": 12, "stato": "in-arrivo"},
        {"titolo": "Manutenzione Caldaia", "condominio": "Condominio Napoli", "giorni": -2, "stato": "scaduto"}
    ]
    
    return render_template('index.html', riepilogo=dati_riepilogo, scadenze=scadenze)

if __name__ == '__main__':
    app.run(debug=True)