from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    try:
        conn = sqlite3.connect('gerenciamento_alunos.db')
        conn.row_factory = sqlite3.Row  # Melhor formato para acessar os dados
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Criar tabelas se não existirem
def criar_tabelas():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                matricula TEXT UNIQUE NOT NULL,
                curso TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER,
                disciplina TEXT NOT NULL,
                nota INTEGER NOT NULL,
                FOREIGN KEY (aluno_id) REFERENCES alunos (id)
            )
        ''')
        conn.commit()
        conn.close()

criar_tabelas()

# Rota principal para listar alunos
@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alunos')
        alunos = cursor.fetchall()
        conn.close()
        return render_template('index.html', alunos=alunos)
    return "Erro ao carregar dados.", 500

# Rota para adicionar novo aluno
@app.route('/novo_aluno', methods=['GET', 'POST'])
def novo_aluno():
    if request.method == 'POST':
        nome = request.form.get('nome')
        matricula = request.form.get('matricula')
        curso = request.form.get('curso')

        if not nome or not matricula or not curso:
            return "Todos os campos devem ser preenchidos.", 400

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO alunos (nome, matricula, curso) VALUES (?, ?, ?)', (nome, matricula, curso))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
            except sqlite3.IntegrityError:
                return "Erro: matrícula duplicada.", 400
        return "Erro ao salvar os dados.", 500
    return render_template('novo_aluno.html')

# Rota para adicionar notas para um aluno
@app.route('/adicionar_nota/<int:aluno_id>', methods=['GET', 'POST'])
def adicionar_nota(aluno_id):
    if request.method == 'POST':
        disciplina = request.form.get('disciplina')
        nota = request.form.get('nota')

        if not disciplina or not nota or not nota.isdigit():
            return "Todos os campos devem ser preenchidos corretamente.", 400

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO notas (aluno_id, disciplina, nota) VALUES (?, ?, ?)', (aluno_id, disciplina, int(nota)))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
            except sqlite3.Error as e:
                return f"Erro ao salvar os dados: {e}", 500
    return render_template('adicionar_nota.html', aluno_id=aluno_id)

if __name__ == '__main__':
    app.run(debug=True)