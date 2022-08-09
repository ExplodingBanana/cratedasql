# cratedasql
Holds SQL queries as objects

# How it works
`Query` object initially holds only path to the SQL file. You can load files contents by the `.read()` method. I've separated the procedures in case you store entire fokin' databases in a single file for some reason.

`q = Query("EXAMPLE/PATH").read()` will initialize the Query object and read the file (`q`'s type is still `Query`). 
If you want to sort them based on whether they are loaded or not or some shit like this, there's a boolean `loaded` property for you.

Now to the fun bit. <b>Crate class</b>

To be concise, it's a mess. Initially it holds nothing, an empty array, if you will.
The fun starts at the `pack` method. You can pass a single `Query` or a `list` of them. I didn't bother actually checking the type of what you're trying to pack, so it's on the TODO list. Oh, but if you don't pass anything, it will spit out an error. Also, you can specify if you want the given queries to be loaded with the boolean `read` argument.

If you want to clear out the crate, use the `unpack` method. It returns everything the object contained, just in case.

Now, of course you want to be able to find the necessary query. Introducing, the `find` method. It uses an ingenious system of looping over the whole container and returning the first `Query` with a matching `path`

Once againg, shit like `c = Crate().pack(q)` is accetable and `c` will be of the `Crate` class

See actual code for advanced tips and tricks on rewriting the whole lib yourself.