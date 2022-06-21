init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/lacasarestaurante/$(name)/g' *.* {} \;
	mv ./lacasarestaurante ./$(name)
  

superuser:
	docker exec -it lacasarestaurante ./manage.py createsuperuser

shell:
	docker exec -it lacasarestaurante ./manage.py shell

makemigrations:
	docker exec -it lacasarestaurante ./manage.py makemigrations

migrate:
	docker exec -it lacasarestaurante ./manage.py migrate


initialfixture:
	docker exec -it lacasarestaurante ./manage.py loaddata initial

testfixture:
	docker exec -it lacasarestaurante ./manage.py loaddata test

test:
	docker exec -it lacasarestaurante ./manage.py test

testapp:
	docker exec -it lacasarestaurante ./manage.py test $(app) --noinput -v 3

statics:
	docker exec -it lacasarestaurante ./manage.py collectstatic --noinput

makemessages:
	docker exec -it lacasarestaurante django-admin makemessages

compilemessages:
	docker exec -it lacasarestaurante django-admin compilemessages
