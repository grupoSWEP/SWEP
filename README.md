# SWEP - Software Engineering Project (PTBR - ENG)
Projeto referente à disciplina de Engenharia de Software (Fundamentos de Desenvolvimento de Software)

Tema = Pobreza (ODS1) e Segurança Alimentar (ODS2)

Pergunta norteadora - 'Como podemos ofertar acesso a informações para um melhor ganho nutricional?'

## **SWEP**

This project represents the Backend API to feed
the SWEP application and it's aim to FDS subject.

### **Clone Project**
```
$ git clone https://github.com/levasl/SWEP.git && cd SWEP
```

### **Prepare Enviroment**

> Here we should to make a Virtual Enviroment to run the API and installing Python and DRF libraries into this enviroment.
```
$ python3 -m venv venv
```

> Choose command to activate venv based on your OS
```
$ venv\Scripts\activate.bat // Windows
$ source venv/bin/activate // MacOS and Linux
```

> Now we'll install the dependencies.
```
$ pip install -r requirements.txt
```

### **Migrate Project Models**
```
$ python3 manage.py migrate
```

### **Running Project**
```
$ python3 manage.py runserver
```

### **Accessing the Project**

Access it in following link:
http://localhost:8000/

## Status do projeto
Protótipo lofi aprovado com 7 histórias e a criação de uma 8ª e em andamento para deploy!

## O que o projeto faz? 
A aplicação web terá como função a informação de pessoas em vulnerabilidade social e pobreza nutricional, com o intuito de gerar receitas de baixo custo e alto valor nutricional. Diante disso, quem tiver acesso à aplicação web poderá inserir os alimentos que possui em casa e ela irá elaborar receitas práticas e fáceis de construir com componentes simples, mas atingindo a maior capacidade de valor nutricional possível.
  
## Por que o projeto é útil?
O projeto busca promover a redução dos índices de pobreza nutricional e alimentícia no Brasil, mais especificamente nas regiões norte e nordeste, as quais lidam com os maiores índices acerca desse tema. O projeto torna-se útil por fomentar o crescimento nutricional das camadas mais vulneráveis da população, bem como influencia a melhora de diversas taxas que afetam essa população, como a baixa escolaridade, violência, saúde mental entre outros. 

## Como os usuários podem começar a usufruir o projeto?
O projeto será acessível através de uma plataforma que, sem necessidade de cadastro ou login, solicitará os alimentos disponíveis na residência do usuário e com isso irá calcular receitas com o maior valor nutricional possível, retornando ao usuário os possíveis preparos. O planejamento é de uma plataforma na versão web, também disponibilizada para a instalação em  dispositivos mobile. O objetivo é que o programa seja bem intuitivo, para que possa abranger pessoas de todos os níveis de instrução e acesso à tecnologia, tornando a interação compreensível e simples.

## Como os usuários podem obter ajuda com nosso projeto?
Por intermédio do nosso projeto os usuários terão ajuda no seu dia-a-dia ao passo que ele visa promover uma alimentação saudável com receitas de baixo custo mas sempre promovendo um alto valor nutricional. Dessa forma, nosso projeto estimula um consumo balanceado mesmo com recursos limitados, ajudando, assim, pessoas em vulnerabilidade social. Com isso, os usuários terão uma melhora na sua pobreza nutricional.

## Quem mantém e contribui com o projeto?
O projeto a princípio será mantido pela equipe em colaboração com uma profissional da área de nutrição, responsável pela indicação de receitas com maior equilíbrio nutricional. No decorrer do desenvolvimento, a colaboração será ampliada para receber contribuições de outros nutricionistas e também dos usuários que terão espaço para inserir suas próprias dicas de receitas, com a devida divisão entre receitas de profissionais e de usuários. No desenvolvimento da aplicação estão as estudantes de Ciência da Computação da CESAR School Letícia De Albuquerque, Luiza Omena, Maria Luiza Vasconcelos, Mariana Belo, Marília Santos e Nathália Accioly.

# ENG version 

Project related to the class of Software Engineering (Fundamentals of Software Development)

Key issue = Poverty (SDG1) and Food Security (SDG2)

Guiding question - 'How can we provide access to information for a better nutritional gain?'

## Project Status
Lofi prototype approved with 7 user stories + a new add and in progress to deploy!

## What does the project accomplish?
The web application will have as a main feature information driven to people in social vulnerability and nutricional poverty, with the main goal to generate low-cost recipes with high nutritional value. Said that, the user who accesses it will be able to insert the ingredients they have at home and it will reply with a practical, simple and easy recipe but with the highest nutritional value as possible.
    
## Why is the project useful?
The project aims to decrease nutritional and food poverty levels in Brazil, more specifically in the northern and northeastern regions which suffer the most with this issue. The project becomes useful by fostering the nutritional growth of the most vulnerable layers of the population, as well as influencing the improvement of several rates that affect this population, such as low schooling, violence, mental health, among others.
    
## How can users start enjoying the project?
The project will be available through a platform that, with no need for registration or login, will request the food availability at the user's home and with this will calculate recipes with the highest possible nutritional value, returning to the user the possible recipes. The goal is to have a web version platform, also available for installation on mobile devices. The goal is for the program to be very intuitive, so that it can reach people of all levels of education and access to technology, making interaction understandable and simple.

## How can users get help with our project?
Through our project, users will get help in their daily lives as it aims to promote healthy eating with low-cost recipes but always seeking a high nutritional value. With that being said, our project stimulates a balanced consumption even with limited resources, thus helping people in social vulnerability. With this, users will have a decrease in their nutritional poverty.

## Who maintains and contributes to the project?

At first, the project will be maintained by the team in collaboration with a professional nutritionist, responsible for indicating recipes with better nutritional balance. As the project develops, the collaboration will be expanded to receive contributions from other nutritionists and also from users, who will have space to insert their own recipe tips, with the proper division between professional and user recipes.

CESAR School Computer Science students Letícia De Albuquerque, Luiza Omena, Maria Luiza Vasconcelos, Mariana Belo, Marília Santos, and Nathália Accioly are developing the application.
