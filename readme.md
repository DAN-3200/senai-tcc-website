## App Zendo - projeto TCC SENAI

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

## Descrição

Aplicativo de gestão de tempo e descanso, prototipado com Python, Flask, Html, CSS, JS e MySQL. O aplicativo permite gerenciar notas, cronometrar tarefas e garante um "escape de stress" com a funcionalidade anti-stress. Este app foi desenvolvido para o processo de avaliação acadêmica, TCC final, do curso <strong>Desenvolvimento de Sistemas</strong> do <strong>Senai Feira de Santana</strong>.
 
## Instalação e uso

criar e ativar o ambiente virtual
```cmd
python -m venv venv
```

```cmd
./venv/Scripts/activate
```

###### Instalar dependencias

```cmd
pip install flask flask_sqlalchemy flask_wtf mysql-connector-python flask_login flask_bcrypt flask_migrate
```
 ou
```cmd
pip install -r requeriments.txt
```

###### Executar a aplicação
```powershell
py app.py
```
> [!IMPORTANT]
> Para o funcionamento do app, execute antecipademente o banco de dados 

## Contribuidores

- Isabella Souza
- Anna Clara Caetano
- Daniel Barros Moreira
- João Arthur Soares
- Edmundo Angelo Siqueira

## Fontes

```
https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/ 
https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/#application-factories 
https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/ 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins 
https://stackoverflow.com/questions/19274226/how-to-track-the-current-user-in-flask-login
https://www.youtube.com/playlist?list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX
https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
https://www.youtube.com/watch?v=dCym9EICKGQ&t=590s&pp=ugMICgJwdBABGAHKBQ1mbGFzayBtaWdyYXRl
https://medium.com/@alfatihridhont/flask-chapter-4-database-orm-786f16fd3b59
```

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
