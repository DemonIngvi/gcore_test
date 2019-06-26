# snake api statistic

## Описание
Сервис получения информации о коммите

## Запуск

### Локальный (без использования docker)
python3 setup.py install

сервис будет доступен на 0.0.0.0:4000

### С использванием docker-compose 
  ```BASH
  docker-compose up --build
  ```

### Остановка и удаление контейнера и образа

* Остановка с удалением контейнера
  ```BASH
  docker-compose down
  ```

* Остановка с удалением контейнера и образа
  ```BASH
  docker-compose down --rmi all -v
  ```