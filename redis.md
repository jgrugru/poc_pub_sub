# Redis notes
---------------
## Start commands
 - docker
 `docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest`
 - Starts server as background task
`redis-server --daemonize yes`
 - open the redis-cli
`redis-cli`
 - Test that redis is up
`redis-cli ping`

 - Select db layer, 0-15 are available
```bash
127.0.0.1:6379> incr a
(integer) 1
127.0.0.1:6379> select 1
127.0.0.1:6379[1]> incr a
(integer) 1
```

- use tab for type hints in redis-cli
- see helpful info about current redis state
`redis-cli --stat`
- analyzes keys, shows which are the biggest, etc
`redis-cli --bigkeys`

 - reset the redis databases
   - Reset the current db you are on: `redis-cli FLUSHDB`
   - Reset all the databases: `redis-cli FLUSHALL`


Can interact with redis through cli or code
 - explain get/set
 - `select` statement
 - go through this [link](https://www.digitalocean.com/community/cheatsheets/how-to-manage-redis-databases-and-keys)