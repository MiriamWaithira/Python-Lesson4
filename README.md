# Python-Lesson4
This is the fourth lesson for Python

1. Event.py

Summary: Uses the 'gevent' library to run three tasks concurrently, each pausing (sleeping) for a set amount of time. All tasks are initiated and gevent.joinall waits for each one to complete.
Required Package: 'gevent' use the command- (pip install gevent).
Required extensions: Monkey C v1.0.11 Garmin, Monkey C v0.4.0 Alexander Fedora

2. Webb.py

Summary: A basic web server using 'aiohttp' to handle asynchronous HTTP requests. It responds with "Hello, [name]" (or "Hello, Anonymous" if no name is provided) based on the URL accessed.
Required Package: 'aiohttp' use the command- (pip install aiohttp).

3. Tornado.py

Summary: Uses 'Tornado' to run a web server that responds with "Hello, Kamiri" at the root URL (/). The server listens on port 8888 and uses Tornado’s IOLoop to handle requests asynchronously.
Required Package: 'tornado' use the command- (pip install tornado).

4. Sanic.py

Summary: A simple 'Sanic' application with an endpoint at /hello that returns a JSON message, "Hello, Kamiri. How are you?".
Required Package: 'sanic' use the command- (pip install sanic).