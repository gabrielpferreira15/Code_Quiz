import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestFluxoCompletoQuiz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000/"
        self.driver.implicitly_wait(10)

    def test_fluxo_completo_do_quiz(self):
        driver = self.driver
        
        # --- 1. LOGIN ---
        print("\nIniciando etapa de login...")
        driver.get(self.base_url)
        self.assertIn("Login", driver.title)
        time.sleep(5)

        driver.find_element(By.NAME, "username").send_keys("testeE2E")
        driver.find_element(By.NAME, "password").send_keys("123teste123")
        driver.find_element(By.TAG_NAME, "button").click()
        print("Login realizado.")

        # --- 2. CONFIGURAÇÃO DO QUIZ ---
        WebDriverWait(driver, 10).until(EC.title_contains("Configurar Quiz"))
        print("Página de configuração do quiz carregada.")
        time.sleep(5)

        Select(driver.find_element(By.ID, "linguagem-select")).select_by_visible_text("Python")
        time.sleep(1) 
        Select(driver.find_element(By.ID, "assunto-select")).select_by_visible_text("Sintaxe Básica")
        Select(driver.find_element(By.ID, "dificuldade-select")).select_by_visible_text("Fácil")
        
        driver.find_element(By.ID, "gerar-quiz-btn").click()
        print("Quiz configurado e iniciado.")

        # --- 3. JOGAR O QUIZ ---
        WebDriverWait(driver, 10).until(EC.title_contains("Quiz:"))
        print("Iniciando a resolução do quiz...")

        respostas_corretas_indices = [1, 2, 3, 1, 2] 

        total_perguntas = 5 
        for i in range(total_perguntas):
            print(f"Respondendo pergunta {i+1}/{total_perguntas}...")
            time.sleep(3)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "resposta")))
            opcoes_de_resposta = driver.find_elements(By.NAME, "resposta")
            indice_correto = respostas_corretas_indices[i]
            opcoes_de_resposta[indice_correto].click()
            print(f"Resposta {chr(65 + indice_correto)} selecionada.")

            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(3)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Prosseguir']"))
            ).click()
        
        print("Quiz finalizado.")

        # --- 4. RESULTADOS ---
        WebDriverWait(driver, 10).until(EC.title_contains("Resultado do Quiz"))
        print("Página de resultados carregada.")
        time.sleep(5)

        placar_final_element = driver.find_element(By.TAG_NAME, "h2")
        self.assertIn("Você acertou 5 de 5 perguntas!", placar_final_element.text)
        print(f"Verificação do placar: {placar_final_element.text}")

        # --- 5. RETORNO À CONFIGURAÇÃO ---
        driver.find_element(By.LINK_TEXT, "Tentar outro quiz").click()
        print("Retornando para a página de configuração.")

        # --- 6. LOGOUT ---
        WebDriverWait(driver, 10).until(EC.title_contains("Configurar Quiz"))
        print("Retornou à página de configuração com sucesso!")
        time.sleep(5)

        print("Iniciando etapa de logout...")
        driver.find_element(By.LINK_TEXT, "Sair").click()

        WebDriverWait(driver, 10).until(EC.title_contains("Login"))
        self.assertIn("Login", driver.title)
        print("Logout realizado e retornado à página de login com sucesso!")


    def tearDown(self):
        time.sleep(5) 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)