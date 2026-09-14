class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Extract individual coordinates for readability
        # rec = [x1, y1, x2, y2]
        
        # Check if X-axis intervals overlap
        x_overlap = rec1[0] < rec2[2] and rec2[0] < rec1[2]
        
        # Check if Y-axis intervals overlap
        y_overlap = rec1[1] < rec2[3] and rec2[1] < rec1[3]
        
        # Both must be true for the 2D rectangles to overlap
        return x_overlap and y_overlap
