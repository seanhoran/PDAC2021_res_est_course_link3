def get_text_block(fname):
  # this is how to read a block of text:
  path = "..//PDAC2021_res_est_course_link3/text_blocks"
  f = open(path + "//" + fname, "r")
  # and then write it to the app
  return f.read();
  
