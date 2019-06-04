# on MacOS install the following:
# brew install imagemagick mozjpeg
# ln -s /usr/local/Cellar/mozjpeg/{version}/bin/cjpeg /usr/local/bin/mozcjpeg

require 'pathname'
require 'image_processing/mini_magick'

namespace :images do
  task :resize do
    board_image_path = File.expand_path('../../assets/images/boards', __dir__)

    Pathname.new(board_image_path).children.each do |path|
      next unless path.file?
      puts "processing #{path}"
      small_processed = ImageProcessing::MiniMagick.source(path)
                                                   .resize_to_limit(300, 225)
                                                   .call

      large_processed = ImageProcessing::MiniMagick.source(path)
                                                   .resize_to_limit(800, 600)
                                                   .call

      large_path = File.join(board_image_path, 'large', path.basename)
      small_path = File.join(board_image_path, 'small', path.basename)

      `mozcjpeg -quality 80 -optimize -outfile #{large_path} #{large_processed.path}`
      `mozcjpeg -quality 80 -optimize -outfile #{small_path} #{small_processed.path}`
    end
  end
end
