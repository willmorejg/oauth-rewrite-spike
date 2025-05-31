# Copyright 2025 James G Willmore
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{app_id}")
def custom_docs(app_id: int):
    return {"message": "Welcome to the documentation endpoint! This is a custom message for ID: " + str(app_id)}
