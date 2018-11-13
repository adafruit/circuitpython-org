#!/usr/bin/env ruby

require 'rubygems'
require 'open-uri'
require 'json'
require 'base64'

desc 'Copy files from the newsletter repository'
task :copy_newsletter_posts do
  file = open('https://api.github.com/repos/adafruit/circuitpython-weekly-newsletter/contents/_posts').read

  posts = JSON.parse(file)

  posts.each do |post|
    response = JSON.parse(open(post["url"]).read)
    content = Base64.decode64(response["content"])
    File.write File.join(File.dirname(__FILE__), '../../_posts/', post["name"]), content
    sleep 2
  end
end
