import firebase_admin
from firebase_admin import credentials, firestore

# Firebaseの設定（サービスアカウントキーを使う）
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # ここに正しいパスを指定
firebase_admin.initialize_app(cred)

# Firestoreデータベースに接続
db = firestore.client()

# AIONの思考ログを取得
def get_thought_logs():
    logs_ref = db.collection("thought_logs").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(5)
    docs = logs_ref.stream()
    
    print("最新の思考ログ:")
    for doc in docs:
        log_data = doc.to_dict()
        print(f"🧠 {log_data['timestamp']} - {log_data['content']}")

# 実行
get_thought_logs()
