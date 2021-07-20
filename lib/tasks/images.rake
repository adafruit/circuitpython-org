# on MacOS install the following:
# brew install imagemagick mozjpeg
# ln -s /usr/local/Cellar/mozjpeg/{version}/bin/cjpeg /usr/local/bin/mozcjpeg

require 'pathname'
require 'image_processing/mini_magick'

namespace :images do
  task :resize do
    board_images_path = File.expand_path('../../assets/images/boards', __dir__)
    original_images_path = File.join(board_images_path, 'original')

    Pathname.new(original_images_path).children.each do |path|
      next unless path.file?
      puts "processing #{path}"
      original_image = File.join(original_images_path, path.basename)
      large_image = File.join(board_images_path, 'large', path.basename)
      small_image = File.join(board_images_path, 'small', path.basename)

      small_processed = ImageProcessing::MiniMagick.source(original_image)
                                                   .resize_to_limit(300, 225)
                                                   .call

      large_processed = ImageProcessing::MiniMagick.source(original_image)
                                                   .resize_to_limit(800, 600)
                                                   .call

      `mozcjpeg -quality 80 -optimize -outfile #{large_image} #{large_processed.path}`
      `mozcjpeg -quality 80 -optimize -outfile #{small_image} #{small_processed.path}`
    end
  end
end
