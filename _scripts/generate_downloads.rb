require 'json'
require 'erb'
require 'cgi'

template = ERB.new <<-EOF
---
layout: download
title: "<%= id %> Download"
name: "<%= id %>"
version: "<%= attributes["version"] %>"
manufacturer: "<%= attributes["manufacturer"] %>"
downloads: "<%= attributes["downloads"] %>"
board_url: "<%= attributes["board_url"] %>"
board_image: "<%= attributes["board_image"] %>"
description: "<%= attributes["description"] %>"
files:
  "en": "<%= attributes["files"]["en"] %>"
  "de": "<%= attributes["files"]["de"] %>"
  "es": "<%= attributes["files"]["es"] %>"
  "fil": "<%= attributes["files"]["fil"] %>"
permalink: "/download/<%= CGI.escape(id) %>/"
---
EOF

downloads = File.read('../_data/downloads.json')
downloads = JSON.parse(downloads)

downloads["data"].each do |download|
  path = File.join('../_downloads', "#{CGI.escape(download["id"])}.md")
  File.open(path, 'w') do |f|
    f.write template.result_with_hash(download)
  end
end
