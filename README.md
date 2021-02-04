# Snap-Shipper

An alternative way to upload snapshots that does not involve Google Drive or Dropbox.

**Supports**
- WebDAV (i.e. Nextcloud)
- Amazon S3 Bucket

## Configuration example

```
DryRun: true
Folder: /backup
Sinks:
  - Name: Your Webdav
    WebDavClient:
      webdav_hostname: 'https://Your-domæne/remote.php/dav/files/some-user/backups'
      webdav_login: some-user
      webdav_password: the password
  - Name: AWS S3
    S3Client:
      endpoint_url: 'https://s3.eu-west-1.amazonaws.com'
      aws_access_key: <access key>
      aws_secret_access_key: <secret access key>
      bucket: <bucket name>
```

## Running at an interval

You can run this add-on at an interval using Home Assistant automations. Here's an example:

**Backup snapshots every day at midnight**
```
alias: Backup snapshots
description: ''
trigger:
  - platform: time
    at: '00:00:00'
condition: []
action:
  - service: hassio.snapshot_full
    data: {}
  - service: hassio.addon_start
    data:
      addon: <ADDON_NAME> # to find name, view README.md
mode: single
```

### Finding the `addon` value for an automation

When editing the add-on's configuration or viewing its logs, observe the URL slug and you can find the add-on name:

```
https://your.hassio.domain:8123/hassio/addon/<ADDON_NAME>/logs
```

## Future plans

Add more sink types and add error handling and notifications

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
