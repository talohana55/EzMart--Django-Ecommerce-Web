# EzMart--Django-Ecommerce-Web
Requirements:
1. Stable internet connection
		2. VSCode 
		3. Django web framework
		4. Python 3.3 or after	
		4.1   
        asgiref==3.3.1
        Django==3.1.3
        django-grappelli==2.14.3
        Pillow==8.0.1
        psycopg2==2.8.6
        pytz==2020.4
        sqlparse==0.4.1
		    {django extensions}
        

			Installation:

		1. Install django and VSCode successfully on your machine. (Guides can be found online)
		2. Create a designated folder for the project, make sure 'requirements.txt' is present in it.
		3. Open your designated folder with a windows powershell/cmd (or linux equivalent), run the following commands:
		    -m pip install -r requirements.txt		(Best to run as admin!)
		4. At this point, if the project files aren't already present in the designated folder, copy them in.
		
				
			Running the project:
      
		1. Open the folder in VSCode or CMD, navigate using the VSCode command shell (Or windows command shell) to the path containing
		   the "manage.py" file.
		2. In the shell (under the afformentioned path) run "python manage.py runserver".
		3. This should result in the shell correctly displaying that the server is running, while linking the localhost IP address
		   for the project: 127.0.0.1
		4. Enter the IP in your local browser (preferably chrome), and browse the site! 
