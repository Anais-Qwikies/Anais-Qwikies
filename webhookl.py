// Initialize WebHooks module.
var WebHooks = require('node-webhooks')
 
// Initialize webhooks module from on-disk database
var webHooks = new WebHooks({
    db: './webHooksDB.json', // json file that store webhook URLs
    httpSuccessCodes: [200, 201, 202, 203, 204], //optional success http status codes
})
 
// Alternatively, initialize webhooks module with object; changes will only be
// made in-memory
webHooks = new WebHooks({
    db: {"addPost": ["http://localhost:9100/posts"]}, // just an example
})
 
// sync instantation - add a new webhook called 'shortname1'
webHooks.add('shortname1', 'http://127.0.0.1:9000/prova/other_url').then(function(){
    // done
}).catch(function(err){
    console.log(err)
})
 
// add another webHook
webHooks.add('shortname2', 'http://127.0.0.1:9000/prova2/').then(function(){
    // done
}).catch(function(err){
    console.log(err)
});
 
// remove a single url attached to the given shortname
// webHooks.remove('shortname3', 'http://127.0.0.1:9000/query/').catch(function(err){console.error(err);})
 
// if no url is provided, remove all the urls attached to the given shortname
// webHooks.remove('shortname3').catch(function(err){console.error(err);})
 
// trigger a specific webHook
webHooks.trigger('shortname1', {data: 123})
webHooks.trigger('shortname2', {data: 123456}, {header: 'header'}) // payload will be sent as POST request with JSON body (Content-Type: application/json) and custom header
 