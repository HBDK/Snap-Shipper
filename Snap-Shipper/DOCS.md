## Getting started

Fill out the config and press start

the add on stops when it is done uploading, so to make sure you backups are shipped you must run this manually when a new snapshot is done or set up an automation to trigger this.

I recommend setting DryRun to True until you are sure you configuration is correct

## Options

this project currently doesn't verify the schema of the config so please start the addon after config changes to make sure that they work.

```yaml
DryRun: true
Folder: /backup
Sinks:
  - Name: Your Webdav
    WebDavClient:
      webdav_hostname: "https://Your-domæne/remote.php/dav/files/some-user/backups"
      webdav_login: some-user
      webdav_password: the password

  - Name: AWS S3
    S3Client:
      endpoint_url: "https://s3.eu-west-1.amazonaws.com"
      aws_access_key: <access key>
      aws_secret_access_key: <secret access key>
      bucket: <bucket name>
```

- **Folder**:  
  the folder to process, this should always be /backup

- **DryRun**:  
  if true no files will be uploaded, set to false when you know that everything is configured right

- **Sinks**:  
  A list of sinks, every file will be uploadet to every sink that doesn't allready contain a file with that name. see section sinks for more info

### Sinks

each sink must have a name and a configuration.

the only sink type supported now is Webdav.

#### WebDavClient

The entire contents of this object is passed when creating the sink so for further options please refer to the documentation for [webdavclient3](https://pypi.org/project/webdavclient3/)

#### S3Client

The S3 client can upload snapshots to any S3 compatible storage (e.g. AWS S3, Backblaze).

- **endpoint_url**:
  The URL of the storage provider. For AWS S3, this follows the schema `https://s3.<region-code>.amazonaws.com`, see [AWS docs](https://docs.aws.amazon.com/general/latest/gr/rande.html)

## License

MIT License

Copyright (c) 2020 Harald Bildsøe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
