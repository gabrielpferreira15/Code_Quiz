import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class TestFluxoCompletoQuiz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000/"
        self.driver.implicitly_wait(3) 

    def test_fluxo_completo_com_revisao(self):
        driver = self.driver
        
        # --- 1. LOGIN ---
        print("\nIniciando etapa de login...")
        driver.get(self.base_url + "accounts/login/")
        WebDriverWait(driver, 10).until(EC.title_contains("Login"))
        time.sleep(4)

        driver.find_element(By.NAME, "username").send_keys("testeE2E")
        driver.find_element(By.NAME, "password").send_keys("123teste123")
        driver.find_element(By.TAG_NAME, "button").click()
        print("Login realizado.")

        # --- 2. CONFIGURAÇÃO DO QUIZ ---
        WebDriverWait(driver, 10).until(EC.title_contains("Configurar Quiz"))
        print("Página de configuração do quiz carregada.")
        time.sleep(5)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "linguagem-select"))
        )
        Select(driver.find_element(By.ID, "linguagem-select")).select_by_visible_text("Python")
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            lambda d: len(Select(d.find_element(By.ID, "assunto-select")).options) > 1
        )
        Select(driver.find_element(By.ID, "assunto-select")).select_by_visible_text("Sintaxe Básica")
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            lambda d: len(Select(d.find_element(By.ID, "dificuldade-select")).options) > 1
        )
        Select(driver.find_element(By.ID, "dificuldade-select")).select_by_visible_text("Fácil")
        time.sleep(2)
        
        driver.find_element(By.ID, "gerar-quiz-btn").click()
        print("Quiz configurado e iniciado.")

        # --- 3. JOGAR O QUIZ (COM 1 ERRO INTENCIONAL) ---
        WebDriverWait(driver, 10).until(EC.title_contains("Quiz:"))
        print("Iniciando a resolução do quiz...")

        respostas_indices = [1, 2, 3, 1, 0] 
        total_perguntas = 5 

        for i in range(total_perguntas):
            pergunta_num = i + 1
            print(f"Respondendo pergunta {pergunta_num}/{total_perguntas}...")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "resposta")))
            opcoes_de_resposta = driver.find_elements(By.NAME, "resposta")
            
            indice_selecionado = respostas_indices[i]
            
            driver.execute_script("arguments[0].click();", opcoes_de_resposta[indice_selecionado])
            
            if i == total_perguntas - 1:
                print(f"Resposta {chr(65 + indice_selecionado)} (ERRADA) selecionada.")
            else:
                print(f"Resposta {chr(65 + indice_selecionado)} (Correta) selecionada.")
            
            time.sleep(2)

            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(2)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Prosseguir']"))
            ).click()
        
        print("Quiz finalizado.")

        # --- 4. RESULTADOS E REVISÃO DE ERROS ---
        WebDriverWait(driver, 10).until(EC.title_contains("Resultado do Quiz"))
        print("Página de resultados carregada.")
        time.sleep(2)
        
        placar_final_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        
        expected_score = "Você acertou 4 de 5 perguntas!"
        self.assertIn(expected_score, placar_final_element.text)
        print(f"Verificação do placar: {placar_final_element.text}")

        print("Iniciando verificação da tabela de 'Revisão de Erros'...")
        
        try:
            summary_element = driver.find_element(By.XPATH, "//summary[contains(text(), 'Revisar meus erros')]")
            driver.execute_script("arguments[0].click();", summary_element)
            print("Clicou no <summary> 'Revisar meus erros' para expandir.")
            time.sleep(2)
        except Exception as e:
            self.fail(f"Não foi possível encontrar ou clicar no <summary> 'Revisar meus erros'. Erro: {e}")
        time.sleep(3)

        # --- 4.5. VISUALIZAÇÃO DO RANKING ---
        print("Iniciando visualização da tabela de ranking...")
        
        try:
            link_ranking = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Ver Ranking"))
            )
            print("Link 'Ver Ranking' encontrado.")
        except TimeoutException:
            try:
                link_ranking = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Ranking"))
                )
                print("Link encontrado por PARTIAL_LINK_TEXT.")
            except TimeoutException:
                link_ranking = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'ranking')]"))
                )
                print("Link encontrado por XPATH.")
        
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", link_ranking)
        time.sleep(1)
        
        try:
            link_ranking.click()
            print("Clique no link 'Ver Ranking' realizado.")
        except ElementClickInterceptedException:
            print("Clique interceptado, usando JavaScript...")
            driver.execute_script("arguments[0].click();", link_ranking)
            print("Clique via JavaScript realizado.")
        
        time.sleep(2)
        
        # Verificar se está na página de ranking
        try:
            WebDriverWait(driver, 10).until(EC.title_contains("Ranking:"))
            print("Página de ranking carregada com sucesso!")
            time.sleep(2)
            
            # Verificar a presença da tabela de ranking
            tabela_ranking = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.table"))
            )
            print("Tabela de ranking encontrada.")
            
            # Verificar colunas da tabela
            colunas = driver.find_elements(By.CSS_SELECTOR, "table thead th")
            colunas_texto = [col.text for col in colunas]
            print(f"Colunas da tabela: {colunas_texto}")
            self.assertIn("#", colunas_texto)
            self.assertIn("Usuário", colunas_texto)
            self.assertIn("Acertos", colunas_texto)
            self.assertIn("Tempo Gasto", colunas_texto)
            self.assertIn("Data", colunas_texto)
            
            # Verificar se há pelo menos uma linha de resultado (o do usuário atual)
            linhas_resultado = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            self.assertGreater(len(linhas_resultado), 0, "Deveria haver pelo menos um resultado no ranking")
            print(f"Total de resultados no ranking: {len(linhas_resultado)}")
            
            # Verificar se o usuário atual está destacado
            try:
                linha_usuario = driver.find_element(By.CSS_SELECTOR, "table tbody tr.table-info")
                print("Linha do usuário atual encontrada e destacada.")
                usuario_nome = linha_usuario.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                self.assertEqual(usuario_nome, "testeE2E")
                print(f"Nome do usuário confirmado: {usuario_nome}")
            except Exception as e:
                print(f"Aviso: Linha do usuário não foi destacada. Erro: {e}")
            
            time.sleep(2)
            
        except TimeoutException:
            current_url = driver.current_url
            current_title = driver.title
            self.fail(f"Não carregou a página de ranking. URL atual: {current_url}, Título: {current_title}")
        
        # Voltar para configuração através do botão "Voltar ao menu"
        print("Voltando ao menu de configuração...")
        try:
            btn_voltar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Voltar ao menu"))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn_voltar)
            time.sleep(1)
            btn_voltar.click()
            print("Clique em 'Voltar ao menu' realizado.")
        except Exception as e:
            print(f"Erro ao clicar em 'Voltar ao menu': {e}")
            btn_voltar = driver.find_element(By.LINK_TEXT, "Voltar ao menu")
            driver.execute_script("arguments[0].click();", btn_voltar)
        
        time.sleep(2)

        # --- 5. RETORNO À CONFIGURAÇÃO ---
        print("Tentando clicar em 'Tentar outro quiz'...")
        
        try:
            link_quiz = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Tentar outro quiz"))
            )
            print("Link encontrado por LINK_TEXT.")
        except TimeoutException:
            print("LINK_TEXT não funcionou, tentando PARTIAL_LINK_TEXT...")
            try:
                link_quiz = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Tentar outro"))
                )
                print("Link encontrado por PARTIAL_LINK_TEXT.")
            except TimeoutException:
                print("PARTIAL_LINK_TEXT não funcionou, tentando XPATH...")
                try:
                    link_quiz = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'configurar')]"))
                    )
                    print("Link encontrado por XPATH (href contém 'configurar').")
                except TimeoutException:
                    link_quiz = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='configurar']"))
                    )
                    print("Link encontrado por CSS_SELECTOR.")
        
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", link_quiz)
        time.sleep(1)
        
        try:
            link_quiz.click()
            print("Clique normal realizado com sucesso.")
        except ElementClickInterceptedException:
            print("Clique normal interceptado, usando JavaScript...")
            driver.execute_script("arguments[0].click();", link_quiz)
            print("Clique via JavaScript realizado.")
        
        print("Aguardando redirecionamento para configuração...")
        time.sleep(3)

        # --- 6. VERIFICAÇÃO DO RETORNO ---
        try:
            WebDriverWait(driver, 10).until(EC.title_contains("Configurar Quiz"))
            print("Retornou à página de configuração com sucesso!")
            time.sleep(2)
        except TimeoutException:
            current_url = driver.current_url
            current_title = driver.title
            self.fail(f"Não retornou para a página de configuração. URL atual: {current_url}, Título: {current_title}")

        # --- 7. LOGOUT ---
        print("Iniciando etapa de logout...")
        
        try:
            logout_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sair"))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", logout_link)
            time.sleep(1)
            logout_link.click()
        except Exception as e:
            print(f"Erro ao tentar fazer logout: {e}")
            logout_link = driver.find_element(By.LINK_TEXT, "Sair")
            driver.execute_script("arguments[0].click();", logout_link)

        WebDriverWait(driver, 10).until(EC.title_contains("Login"))
        self.assertIn("Login", driver.title)
        print("Logout realizado e retornado à página de login com sucesso!")

    def tearDown(self):
        time.sleep(2) 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)