import requests
import time
import schedule

def keep_alive(url):
    try:
        response = requests.get(url)
        print(f"Solicitud enviada a {url}. Estado: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error al enviar la solicitud: {e}")

def main():
    # URL de tu aplicación Streamlit
    app_url = "https://claudepdfseptiembre-7jfrpdrpmkfamc4ue8ikv6.streamlit.app/"
    
    # Programar la tarea para que se ejecute cada 5 minutos
    schedule.every(5).minutes.do(keep_alive, url=app_url)
    
    print(f"Iniciando script para mantener activa la aplicación en {app_url}")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
