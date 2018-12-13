#!/usr/bin/env ruby

require 'json'
require 'erb'
require 'cgi'

desc 'Generate download pages from the downloads json file'
task :generate_downloads do

template = <<-EOF
---
# NOTE: The front matter in this file is pre-generated with generate_downloads.rake
# Do not hand edit any of the front matter. You can change these values
# in _data/metadata.json for each respective board
layout: download
board_id: "<%= id %>"
downloads: <%= downloads %>
title: "<%= attributes["name"] %> Download"
name: "<%= attributes["name"] %>"
manufacturer: "<%= attributes["manufacturer"] %>"
board_url: "<%= attributes["board_url"] %>"
board_image: "<%= attributes["board_image"] %>"
permalink: "<%= attributes["permalink"] %>"
---
EOF

  erb = ERB.new(template, nil, '-')

  files = File.read(File.join(File.dirname(__FILE__), '../../_data/files.json'))
  files = JSON.parse(files)

  metadata = File.read(File.join(File.dirname(__FILE__), '../../_data/metadata.json'))
  metadata = JSON.parse(metadata)

  path = File.dirname(__FILE__), '../../_downloads/'

  metadata['data'].each do |data|
    id = data['id']
    file_path = File.join(path, "#{CGI.escape(id)}.#{extension(data)}")
    board = files[id]

    new_contents = erb.result_with_hash(data.merge(board))
    new_contents = merge_content(new_contents, file_path)

    File.open(file_path, 'w') do |f|
      f.write new_contents
    end
  end
end

def merge_content(new_contents, file_path)
  if File.file?(file_path)
    contents = File.read(file_path)
    contents.gsub(/---\n(.)+---\n/m, new_contents)
  else
    new_contents << "\n\nManually add a description here."
  end
end

def extension(data)
  if data['attributes']['description_type'].eql?('markdown')
    'md'
  else
    data['attributes']['description_type']
  end
end
