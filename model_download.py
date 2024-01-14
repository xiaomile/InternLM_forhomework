# 下载InternLM-chat-7b模型
import torch
#from modelscope import snapshot_download, AutoModel, AutoTokenizer
#model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b', cache_dir='/home/xlab-app-center/model', revision='v1.0.3')

from openxlab.model import download 
download(model_repo='xiaomile/personal_assistant2',output='/home/xlab-app-center/model')
