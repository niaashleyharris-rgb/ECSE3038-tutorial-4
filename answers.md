Note - I restarted my server after task 2, so my hardcode is back to 5 devices

After the first post request, I got a 201 created status code and had 6 devices total in the get request including 1 probe object.

After the second post request I got another 201 created status and had 7  devices total from the get request including 2 probe objects.

Note - Had to restart the server again, so starting with 5 devices again

After the first attic put request I got a 200 OK status code and the get reuqest returned 5 devices including the updated attic dictionary. 

After the second attic put request I got 200 OK status code again and the same 5 devices from the get request as before.

After the first send of the the delete request for fridge I got a 200 OK and the get request returned 4 devices exluding the fridge.

After the second send of the delete request for fridge I got a 404 Not Found and the ger request returned the same 4 devices.


The state of the server remained the same for both the put request and delete requests when done repetitively. This is because the put requests updates instead of adds a new object, while the delete request cannot delete an item that no longer exsists, so there is no change to the server.  Hence, the put and get requests are idempotenent. 

Meanwhile, a repetition of the post request resulted in a change in the server's state. This is because this request adds a new object each time rather than overwriting, so the server will gain an additional device each time the post request is made, even if is an identical request. 