# ItemTree Server [![tag](https://img.shields.io/github/tag/namelivia/itemtree-server.svg)](https://github.com/namelivia/itemtree-server/releases) [![Build](https://github.com/namelivia/itemtree-server/workflows/Build/badge.svg)](https://github.com/namelivia/itemtree-server/actions?query=workflow%3ABuild) [![codecov](https://codecov.io/gh/namelivia/itemtree-server/branch/master/graph/badge.svg)](https://codecov.io/gh/namelivia/itemtree-server)

![Item Tree management app](https://user-images.githubusercontent.com/1571416/109545697-797a3780-7ac9-11eb-8c40-ae14573430d9.png)

Backend for an item management app in the form of a tree of items, also an exercise to try FastAPI.

To start the application locally:

```
docker-compose up
```



To run the tests:
```
./run_tests
```

To generate migrations:
```
./run_alembic "YOUR MIGRATION MESSAGE"
```
