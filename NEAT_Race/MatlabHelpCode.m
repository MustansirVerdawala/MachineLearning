%%

clear, clc, close force all;

%%

img=imread("../../../Desktop/DeepReinforcementLearning/ai-car-simulation/map4.png");

% Read the content of the RTF file
rtfContent = fileread("../../../Desktop/DeepReinforcementLearning/ai-car-simulation/ProgressMap4.rtf");  % Specify the path to your RTF file

% Use regular expression to match the coordinates in the format ((x1, y1), (x2, y2))
pattern = '\(\((\d+),\s*(\d+)\),\s*\((\d+),\s*(\d+)\)\)';
matches = regexp(rtfContent, pattern, 'tokens');

% Convert the matches to the desired MATLAB cell array format
coordinates = cellfun(@(x) [str2double(x{1}), str2double(x{2}); str2double(x{3}), str2double(x{4})], matches, 'UniformOutput', false);

%%

for i = 1:length(coordinates)
    % Extract the coordinates for the current pair of points
    coords = coordinates{i};
    x = coords(:, 1); % X coordinates
    y = coords(:, 2); % Y coordinates
    
    % Overlay the line on the image by setting pixel values to white
    for j = 1:length(x)
        img = insertShape(img, 'Line', [x(1) y(1) x(2) y(2)], 'Color', 'white', 'LineWidth', 2);
    end
end

imshow(img);

%%