from mysql.connector import Error

from connection_dao import close_connection, get_connection

def inserir_planta(nome, especie, preco, estoque):
    conn = get_connection()

    if conn is None:
        return None

    cursor = None

    try:
        cursor = conn.cursor()

        sql = """
            INSERT INTO planta (nome, especie, preco, estoque)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (nome, especie, preco, estoque))
        conn.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Erro ao inserir planta: {e}")
        conn.rollback()
        return None

    finally:
        close_connection(conn, cursor)

def listar_plantas():
    conn = get_connection()

    if conn is None:
        return []

    cursor = None

    try:
        cursor = conn.cursor()

        sql = "SELECT id, nome, especie, preco, estoque FROM planta ORDER BY id"

        cursor.execute(sql)

        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao listar plantas: {e}")
        return []

    finally:
        close_connection(conn, cursor)

def buscar_por_especie(especie):
    conn = get_connection()

    if conn is None:
        return []

    cursor = None

    try:
        cursor = conn.cursor()

        sql = "SELECT id, nome, especie, preco, estoque FROM planta WHERE especie = %s"

        cursor.execute(sql, (especie,))

        return cursor.fetchall()

    except Error as e:
        print(f"Erro ao buscar plantas: {e}")
        return []

    finally:
        close_connection(conn, cursor)

def atualizar_preco(id_planta, novo_preco):
    conn = get_connection()

    if conn is None:
        return False

    cursor = None

    try:
        cursor = conn.cursor()

        sql = "UPDATE planta SET preco = %s WHERE id = %s"

        cursor.execute(sql, (novo_preco, id_planta))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao atualizar preco: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)

def remover_planta(id_planta):
    conn = get_connection()

    if conn is None:
        return False

    cursor = None

    try:
        cursor = conn.cursor()

        sql = "DELETE FROM planta WHERE id = %s"

        cursor.execute(sql, (id_planta,))
        conn.commit()

        return cursor.rowcount > 0

    except Error as e:
        print(f"Erro ao remover planta: {e}")
        conn.rollback()
        return False

    finally:
        close_connection(conn, cursor)

def valor_total_estoque():
    conn = get_connection()

    if conn is None:
        return 0.0

    cursor = None

    try:
        cursor = conn.cursor()

        sql = "SELECT COALESCE(SUM(preco * estoque), 0) FROM planta"

        cursor.execute(sql)

        resultado = cursor.fetchone()

        return float(resultado[0])

    except Error as e:
        print(f"Erro ao calcular estoque: {e}")
        return 0.0

    finally:
        close_connection(conn, cursor)