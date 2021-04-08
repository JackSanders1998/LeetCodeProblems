class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_track = []
        zig = True
        zag = False
        row_length = 0
        zag_index = numRows-2
        while len(s) > 0:
            if zig == True:
                try:
                    row_track.append({"key": "zig", "val": s[0:numRows]})
                    s = s[numRows:]
                except:
                    row_track.append(s[numRows:])
            elif zag == True:
                for i in range(numRows-2):
                    if len(s) > 0:
                        row_track.append({"key": "zag", "val": s[0], "index": zag_index-i})
                        s = s[1:]
            swap = zag
            zag = zig
            zig = swap
        
        output = ""
        for row in row_track:
            if row["key"] == "zag":
                row["val"] = " " * row["index"] + row["val"]
        
        for i in range(numRows):
            for row in row_track:
                if len(row["val"]) > 0:
                    output += row["val"][0]
                    row["val"] = row["val"][1:]
                
        final_string = ""
        for val in output.split():
            final_string += val
        return final_string
