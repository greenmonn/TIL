# Content-type in HTTP headers

The `Content-Type` entity header is used to indicate the **media type** of the resource.

## Prevent MIME sniffing
Browsers will do *MIME sniffing* in some cases and will not necessarily follow the value of this header; to prevent this behavior, the header `X-Content-Type-Options` can be set to `nosniff`.

> MIME sniffing: Content sniffing, also known as media type sniffing or MIME sniffing, is the practice of inspecting the content of a byte stream to attempt to deduce the file format of the data within it.

## Syntax

```
Content-Type: text/html; charset=utf-8
Content-Type: multipart/form-data; boundary=something
```

## Directives
### media-type
The *MIME type* of the resource of the data

>  MIME type: Multipurpose Internet Mail Extensions (MIME) type is a standard that indicates the nature and format of a document, file, or assortment of bytes. 

### charset
The character encoding standard

### boundary
For multipart entities the `boundary` directive is required, which consists of 1 to 70 characters from a set of characters known to be very robust through email gateways, and not ending with white space. It is used to encapsulate the boundaries of the multiple parts of the message. Often the header boundary is prepended by two dashes(--) in the body and the final boundary also have a two dashes appended to it.

## Content-Type on HTTP POST method
- `application/x-www-form-urlencoded`: Encoded to key-value tuple. (splitted by '&', connected by '=') Non-alphabet symbol is percent-encoded. So **this content type is not suitable to binary data**.

- `application/form-data`: can be used for binary data.
- `text/plain`

## Examples
### in HTML forms: enctype
```html
<form action="/" method="post" enctype="multipart/form-data">
  <input type="text" name="description" value="some text">
  <input type="file" name="myFile">
  <button type="submit">Submit</button>
</form>
```

### Parsing `multipart/form-data` in express.js

Use `multer` library to parse `multipart/form-data`.

```javascript
const multer = require('multuer');

const upload = multer({ storage: multer.memoryStorage() });

router.post('/api/image', upload.single('cell'), (req, res) => {
    res.send(req.file) // payload is stored in `req.file.buffer`
});
```

- See also: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type