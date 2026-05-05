#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🪒 الملف السحري الكامل - متجر الحلاقة SO2_MK
Cloudinary: dmla61v7n/so2_mk
Firebase: gomrka-420d0
رمز الإدارة: 1234
"""

import json
import os
from datetime import datetime

# ============================================
# 🔧 الإعدادات
# ============================================
CONFIG = {
    "site_name": "صالون MK للحلاقة",
    "cloudinary_cloud": "dmla61v7n",
    "cloudinary_folder": "so2_mk",
    "firebase_url": "https://gomrka-420d0-default-rtdb.firebaseio.com",
    "admin_password": "1234",
    "currency": "ريال",
    "phone": "0500000000",
    "whatsapp": "966500000000"
}

# ============================================
# 📦 المنتجات الافتراضية
# ============================================
DEFAULT_PRODUCTS = [
    {
        "id": 1,
        "name": "ماكينة حلاقة احترافية X1",
        "price": 299,
        "category": "ماكينات",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product1.jpg",
        "description": "ماكينة حلاقة متطورة للصالونات",
        "stock": 50,
        "rating": 4.8
    },
    {
        "id": 2,
        "name": "طقم أمشاط احترافي 12 قطعة",
        "price": 149,
        "category": "أمشاط",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product2.jpg",
        "description": "مجموعة أمشاط متعددة المقاسات",
        "stock": 100,
        "rating": 4.6
    },
    {
        "id": 3,
        "name": "كريم حلاقة فاخر بالألوفيرا",
        "price": 89,
        "category": "كريمات",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product3.jpg",
        "description": "كريم حلاقة مرطب ومهدئ",
        "stock": 200,
        "rating": 4.9
    },
    {
        "id": 4,
        "name": "فوطة حلاقة قطن مصري",
        "price": 59,
        "category": "فوط",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product4.jpg",
        "description": "فوطة ناعمة 100% قطن",
        "stock": 150,
        "rating": 4.7
    },
    {
        "id": 5,
        "name": "زيت تشحيم ماكينات الحلاقة",
        "price": 45,
        "category": "زيوت",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product5.jpg",
        "description": "زيت خاص لتشحيم وصيانة الماكينات",
        "stock": 300,
        "rating": 4.5
    },
    {
        "id": 6,
        "name": "فرشاة حلاقة من الشعر الطبيعي",
        "price": 120,
        "category": "فرش",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product6.jpg",
        "description": "فرشاة يدوية من شعر الغرير",
        "stock": 75,
        "rating": 4.8
    },
    {
        "id": 7,
        "name": "ماكينة تشذيب اللحية بروفيشنال",
        "price": 199,
        "category": "ماكينات",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product7.jpg",
        "description": "ماكينة تشذيب دقيقة للحية",
        "stock": 80,
        "rating": 4.7
    },
    {
        "id": 8,
        "name": "بخاخ معقم للأدوات",
        "price": 35,
        "category": "معقمات",
        "image": f"https://res.cloudinary.com/{CONFIG['cloudinary_cloud']}/image/upload/v1/{CONFIG['cloudinary_folder']}/product8.jpg",
        "description": "بخاخ تعقيم سريع للأدوات",
        "stock": 500,
        "rating": 4.4
    }
]


def load_products():
    """تحميل المنتجات من الملف المحلي أو إنشاء افتراضية"""
    if os.path.exists('products.json'):
        try:
            with open('products.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                products = data.get('products', [])
                if products:
                    print(f"📦 تم تحميل {len(products)} منتج من products.json")
                    return products
        except:
            pass
    
    print(f"📦 استخدام {len(DEFAULT_PRODUCTS)} منتج افتراضي")
    return DEFAULT_PRODUCTS


def create_index_html(products):
    """إنشاء ملف index.html الكامل"""
    
    products_json = json.dumps(products, ensure_ascii=False)
    
    html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{CONFIG['site_name']} | متجر مستلزمات الحلاقة</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --gold: #c9a96e;
            --dark: #1a1a1a;
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }}
        
        .navbar {{
            background: linear-gradient(135deg, #1a1a1a, #2d2d2d) !important;
            box-shadow: 0 2px 15px rgba(0,0,0,0.3);
            padding: 15px 0;
        }}
        
        .navbar-brand {{
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--gold) !important;
        }}
        
        .nav-link {{
            color: white !important;
            margin: 0 10px;
            transition: 0.3s;
        }}
        
        .nav-link:hover {{ color: var(--gold) !important; }}
        
        .admin-btn {{
            background: var(--gold);
            color: var(--dark);
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }}
        
        .admin-btn:hover {{
            background: #b8963d;
            transform: translateY(-2px);
        }}
        
        .hero {{
            background: linear-gradient(135deg, #1a1a1a 0%, #333 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
        }}
        
        .hero h1 {{
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        
        .hero p {{
            font-size: 1.3rem;
            opacity: 0.9;
        }}
        
        .product-card {{
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            height: 100%;
            position: relative;
        }}
        
        .product-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }}
        
        .product-image-wrapper {{
            position: relative;
            overflow: hidden;
            height: 250px;
        }}
        
        .product-image-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: 0.5s;
        }}
        
        .product-card:hover .product-image-wrapper img {{
            transform: scale(1.1);
        }}
        
        .category-badge {{
            position: absolute;
            top: 15px;
            right: 15px;
            background: var(--gold);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: bold;
        }}
        
        .price-tag {{
            font-size: 1.8rem;
            font-weight: bold;
            color: var(--gold);
            margin: 10px 0;
        }}
        
        .btn-gold {{
            background: var(--gold);
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 25px;
            font-weight: bold;
            transition: 0.3s;
            cursor: pointer;
        }}
        
        .btn-gold:hover {{
            background: #b8963d;
            transform: translateY(-2px);
        }}
        
        .cart-badge {{
            position: absolute;
            top: -8px;
            right: -8px;
            background: #dc3545;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .admin-modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 9999;
            justify-content: center;
            align-items: center;
        }}
        
        .admin-modal.active {{
            display: flex;
        }}
        
        .admin-content {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            width: 90%;
            max-width: 500px;
            animation: slideIn 0.3s ease;
        }}
        
        @keyframes slideIn {{
            from {{ transform: translateY(-50px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}
        
        .quantity-control {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .quantity-control button {{
            width: 30px;
            height: 30px;
            border-radius: 50%;
            border: 2px solid var(--gold);
            background: white;
            color: var(--gold);
            font-size: 1.2rem;
            cursor: pointer;
            transition: 0.3s;
        }}
        
        .quantity-control button:hover {{
            background: var(--gold);
            color: white;
        }}
        
        .quantity-control input {{
            width: 50px;
            text-align: center;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 5px;
        }}
        
        footer {{
            background: var(--dark);
            color: white;
            padding: 30px 0;
            margin-top: 50px;
        }}
        
        .whatsapp-float {{
            position: fixed;
            bottom: 30px;
            left: 30px;
            background: #25d366;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 5px 20px rgba(37, 211, 102, 0.4);
            z-index: 1000;
            transition: 0.3s;
            text-decoration: none;
        }}
        
        .whatsapp-float:hover {{
            transform: scale(1.1);
            color: white;
        }}
        
        .notification {{
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: #28a745;
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            z-index: 10000;
            display: none;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2rem; }}
            .hero p {{ font-size: 1rem; }}
        }}
    </style>
</head>
<body>
    <!-- شريط التنقل -->
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="fas fa-cut"></i> {CONFIG['site_name']}
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="#products">المنتجات</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">من نحن</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">اتصل بنا</a></li>
                </ul>
                <div class="d-flex gap-2">
                    <button class="admin-btn" onclick="openAdminPanel()">
                        <i class="fas fa-plus-circle"></i> إضافة منتج
                    </button>
                    <button class="btn btn-outline-light position-relative" data-bs-toggle="modal" data-bs-target="#cartModal">
                        <i class="fas fa-shopping-cart"></i>
                        <span class="cart-badge" id="cartCount">0</span>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- نافذة الإدارة -->
    <div class="admin-modal" id="adminModal">
        <div class="admin-content">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h3><i class="fas fa-lock"></i> لوحة الإدارة</h3>
                <button class="btn-close" onclick="closeAdminPanel()"></button>
            </div>
            
            <div id="passwordSection">
                <div class="text-center mb-4">
                    <i class="fas fa-key" style="font-size: 3rem; color: var(--gold);"></i>
                    <h4 class="mt-3">أدخل رمز التحقق</h4>
                </div>
                <input type="password" id="adminPassword" class="form-control mb-3" placeholder="أدخل الرمز السري">
                <button class="btn btn-gold w-100" onclick="verifyPassword()">
                    <i class="fas fa-check"></i> دخول
                </button>
            </div>
            
            <div id="addProductSection" style="display: none;">
                <h4 class="mb-3"><i class="fas fa-plus-circle"></i> إضافة منتج جديد</h4>
                <form id="addProductForm">
                    <div class="mb-3">
                        <label class="form-label">اسم المنتج</label>
                        <input type="text" class="form-control" id="productName" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">السعر ({CONFIG['currency']})</label>
                        <input type="number" class="form-control" id="productPrice" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">الفئة</label>
                        <select class="form-control" id="productCategory">
                            <option value="ماكينات">ماكينات</option>
                            <option value="أمشاط">أمشاط</option>
                            <option value="كريمات">كريمات</option>
                            <option value="فوط">فوط</option>
                            <option value="زيوت">زيوت</option>
                            <option value="فرش">فرش</option>
                            <option value="معقمات">معقمات</option>
                            <option value="إكسسوارات">إكسسوارات</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">رابط الصورة</label>
                        <input type="url" class="form-control" id="productImage" placeholder="https://res.cloudinary.com/..." required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">الوصف</label>
                        <textarea class="form-control" id="productDescription" rows="2"></textarea>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">المخزون</label>
                        <input type="number" class="form-control" id="productStock" value="100">
                    </div>
                    <button type="submit" class="btn btn-gold w-100">
                        <i class="fas fa-upload"></i> رفع المنتج
                    </button>
                </form>
            </div>
        </div>
    </div>

    <!-- الإشعارات -->
    <div class="notification" id="notification"></div>

    <!-- الهيدر -->
    <header class="hero">
        <div class="container">
            <h1>🪒 أفضل مستلزمات الحلاقة</h1>
            <p>منتجات احترافية للصالونات والحلاقين - جودة عالية وأسعار منافسة</p>
        </div>
    </header>

    <!-- المنتجات -->
    <section id="products" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">
                <i class="fas fa-star" style="color: var(--gold);"></i>
                منتجاتنا
                <i class="fas fa-star" style="color: var(--gold);"></i>
            </h2>
            <div class="row" id="productsContainer"></div>
        </div>
    </section>

    <!-- من نحن -->
    <section id="about" class="py-5 bg-light">
        <div class="container text-center">
            <h2 class="mb-4">من نحن</h2>
            <p class="lead">متخصصون في توفير أفضل أدوات ومستلزمات الحلاقة من ماركات عالمية</p>
            <div class="row mt-4">
                <div class="col-md-4 mb-3">
                    <i class="fas fa-truck" style="font-size: 3rem; color: var(--gold);"></i>
                    <h5>توصيل سريع</h5>
                </div>
                <div class="col-md-4 mb-3">
                    <i class="fas fa-medal" style="font-size: 3rem; color: var(--gold);"></i>
                    <h5>جودة عالية</h5>
                </div>
                <div class="col-md-4 mb-3">
                    <i class="fas fa-headset" style="font-size: 3rem; color: var(--gold);"></i>
                    <h5>دعم فني</h5>
                </div>
            </div>
        </div>
    </section>

    <!-- اتصل بنا -->
    <section id="contact" class="py-5">
        <div class="container">
            <h2 class="text-center mb-4">اطلب الآن</h2>
            <form id="orderForm" class="row g-3">
                <div class="col-md-6">
                    <input type="text" class="form-control" id="customerName" placeholder="الاسم الكامل" required>
                </div>
                <div class="col-md-6">
                    <input type="tel" class="form-control" id="customerPhone" placeholder="رقم الهاتف" required>
                </div>
                <div class="col-12">
                    <textarea class="form-control" id="orderDetails" rows="3" placeholder="تفاصيل الطلب"></textarea>
                </div>
                <div class="col-12 text-center">
                    <button type="submit" class="btn btn-gold btn-lg">إرسال الطلب</button>
                </div>
            </form>
        </div>
    </section>

    <!-- مودال السلة -->
    <div class="modal fade" id="cartModal">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">🛒 سلة التسوق</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body" id="cartItems">
                    <p class="text-center text-muted">السلة فارغة</p>
                </div>
                <div class="modal-footer">
                    <button class="btn btn-gold" id="checkoutBtn">إتمام الطلب</button>
                </div>
            </div>
        </div>
    </div>

    <!-- زر الواتساب -->
    <a href="https://wa.me/{CONFIG['whatsapp']}" class="whatsapp-float" target="_blank">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- Footer -->
    <footer>
        <div class="container text-center">
            <p>&copy; 2024 {CONFIG['site_name']} - جميع الحقوق محفوظة</p>
            <p>📞 {CONFIG['phone']}</p>
        </div>
    </footer>

    <!-- Firebase SDK -->
    <script src="https://www.gstatic.com/firebasejs/9.6.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.0/firebase-database-compat.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        const firebaseConfig = {{
            apiKey: "AIzaSyDglVPQIfa9bB_ItiQhkkMMxArTPYEGlPY",
            authDomain: "gomrka-420d0.firebaseapp.com",
            databaseURL: "{CONFIG['firebase_url']}",
            projectId: "gomrka-420d0",
            storageBucket: "gomrka-420d0.appspot.com",
            messagingSenderId: "1085915474095",
            appId: "1:1085915474095:web:96751b66e7d2f15d09d35a"
        }};
        
        firebase.initializeApp(firebaseConfig);
        const database = firebase.database();
        
        let products = {products_json};
        let cart = [];
        const CURRENCY = "{CONFIG['currency']}";
        const ADMIN_PASS = "{CONFIG['admin_password']}";
        
        function loadProducts() {{
            const container = document.getElementById("productsContainer");
            
            if (!products || products.length === 0) {{
                container.innerHTML = "<div class='col-12 text-center'><p>لا توجد منتجات حالياً</p></div>";
                return;
            }}
            
            let html = "";
            products.forEach(function(product) {{
                const stars = "⭐".repeat(Math.floor(product.rating || 5));
                html += `<div class="col-md-4 col-lg-3 mb-4">
                    <div class="product-card">
                        <div class="product-image-wrapper">
                            <img src="${{product.image}}" alt="${{product.name}}" onerror="this.src='https://via.placeholder.com/300?text=No+Image'">
                            <span class="category-badge">${{product.category || 'عام'}}</span>
                        </div>
                        <div class="card-body p-3">
                            <h5 class="card-title">${{product.name}}</h5>
                            <div class="mb-1" style="color: #ffc107;">${{stars}} (${{product.rating || 5}})</div>
                            <p class="price-tag">${{product.price}} ${{CURRENCY}}</p>
                            <p class="text-muted small">${{product.description || ''}}</p>
                            <p class="small">📦 المخزون: ${{product.stock || 0}}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="quantity-control">
                                    <button onclick="changeQty(${{product.id}}, -1)">-</button>
                                    <input type="number" id="qty-${{product.id}}" value="1" min="1" max="${{product.stock || 10}}" readonly>
                                    <button onclick="changeQty(${{product.id}}, 1)">+</button>
                                </div>
                                <button class="btn btn-gold" onclick="addToCart(${{product.id}})">
                                    <i class="fas fa-cart-plus"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>`;
            }});
            
            container.innerHTML = html;
            localStorage.setItem("products", JSON.stringify(products));
        }}
        
        function changeQty(productId, delta) {{
            const input = document.getElementById("qty-" + productId);
            let value = parseInt(input.value) + delta;
            const product = products.find(function(p) {{ return p.id === productId; }});
            const maxStock = product ? product.stock : 10;
            if (value < 1) value = 1;
            if (value > maxStock) value = maxStock;
            input.value = value;
        }}
        
        function addToCart(productId) {{
            const product = products.find(function(p) {{ return p.id === productId; }});
            if (!product) return;
            
            const quantity = parseInt(document.getElementById("qty-" + productId).value);
            const existingItem = cart.find(function(item) {{ return item.id === productId; }});
            
            if (existingItem) {{
                existingItem.quantity += quantity;
            }} else {{
                cart.push({{
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    image: product.image,
                    quantity: quantity
                }});
            }}
            
            updateCartCount();
            showNotification("✅ تمت الإضافة إلى السلة!");
        }}
        
        function updateCartCount() {{
            const count = cart.reduce(function(sum, item) {{ return sum + item.quantity; }}, 0);
            document.getElementById("cartCount").textContent = count;
        }}
        
        function displayCart() {{
            const cartContainer = document.getElementById("cartItems");
            
            if (cart.length === 0) {{
                cartContainer.innerHTML = "<p class='text-center text-muted'>السلة فارغة</p>";
                return;
            }}
            
            let total = 0;
            let html = "";
            cart.forEach(function(item, index) {{
                const itemTotal = item.price * item.quantity;
                total += itemTotal;
                html += `<div class="d-flex justify-content-between align-items-center mb-3 border-bottom pb-2">
                    <div>
                        <h6>${{item.name}}</h6>
                        <small>${{item.quantity}} × ${{item.price}} = ${{itemTotal}} ${{CURRENCY}}</small>
                    </div>
                    <button class="btn btn-sm btn-danger" onclick="removeFromCart(${{index}})">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>`;
            }});
            
            html += `<div class="text-end mt-3">
                <h5>المجموع: <span style="color: var(--gold);">${{total}} ${{CURRENCY}}</span></h5>
            </div>`;
            
            cartContainer.innerHTML = html;
        }}
        
        function removeFromCart(index) {{
            cart.splice(index, 1);
            updateCartCount();
            displayCart();
        }}
        
        function openAdminPanel() {{
            document.getElementById("adminModal").classList.add("active");
            document.getElementById("passwordSection").style.display = "block";
            document.getElementById("addProductSection").style.display = "none";
            document.getElementById("adminPassword").value = "";
        }}
        
        function closeAdminPanel() {{
            document.getElementById("adminModal").classList.remove("active");
        }}
        
        function verifyPassword() {{
            const password = document.getElementById("adminPassword").value;
            if (password === ADMIN_PASS) {{
                document.getElementById("passwordSection").style.display = "none";
                document.getElementById("addProductSection").style.display = "block";
                showNotification("✅ تم التحقق بنجاح!");
            }} else {{
                showNotification("❌ رمز خاطئ!", "error");
            }}
        }}
        
        document.getElementById("addProductForm").addEventListener("submit", async function(e) {{
            e.preventDefault();
            
            const newProduct = {{
                id: products.length > 0 ? Math.max(...products.map(p => p.id)) + 1 : 1,
                name: document.getElementById("productName").value,
                price: parseInt(document.getElementById("productPrice").value),
                category: document.getElementById("productCategory").value,
                image: document.getElementById("productImage").value,
                description: document.getElementById("productDescription").value,
                stock: parseInt(document.getElementById("productStock").value),
                rating: 5.0,
                created_at: new Date().toISOString()
            }};
            
            products.push(newProduct);
            
            try {{
                await database.ref("products/" + newProduct.id).set(newProduct);
            }} catch(e) {{}}
            
            loadProducts();
            updateCartCount();
            closeAdminPanel();
            showNotification("✅ تمت إضافة المنتج بنجاح!");
            localStorage.setItem("products", JSON.stringify(products));
            this.reset();
        }});
        
        document.getElementById("orderForm").addEventListener("submit", async function(e) {{
            e.preventDefault();
            
            const order = {{
                customerName: document.getElementById("customerName").value,
                customerPhone: document.getElementById("customerPhone").value,
                orderDetails: document.getElementById("orderDetails").value,
                cart: cart,
                total: cart.reduce((sum, item) => sum + (item.price * item.quantity), 0),
                timestamp: firebase.database.ServerValue.TIMESTAMP,
                status: "جديد"
            }};
            
            try {{
                await database.ref("orders").push(order);
                showNotification("✅ تم إرسال الطلب بنجاح! سنتواصل معك قريباً");
                this.reset();
                cart = [];
                updateCartCount();
                displayCart();
            }} catch(error) {{
                showNotification("❌ حدث خطأ، حاول مرة أخرى", "error");
            }}
        }});
        
        document.getElementById("checkoutBtn").addEventListener("click", function() {{
            if (cart.length === 0) {{
                showNotification("⚠️ السلة فارغة!", "error");
                return;
            }}
            const modal = bootstrap.Modal.getInstance(document.getElementById("cartModal"));
            modal.hide();
            document.getElementById("orderDetails").value = cart.map(item => 
                `${{item.name}} (${{item.quantity}}×)`
            ).join("\\n");
            document.getElementById("contact").scrollIntoView({{ behavior: "smooth" }});
        }});
        
        document.getElementById("cartModal").addEventListener("show.bs.modal", displayCart);
        
        document.getElementById("adminModal").addEventListener("click", function(e) {{
            if (e.target === this) closeAdminPanel();
        }});
        
        function showNotification(message, type) {{
            const notification = document.getElementById("notification");
            notification.textContent = message;
            notification.style.background = type === "error" ? "#dc3545" : "#28a745";
            notification.style.display = "block";
            setTimeout(function() {{
                notification.style.display = "none";
            }}, 3000);
        }}
        
        const savedProducts = localStorage.getItem("products");
        if (savedProducts && products.length === 0) {{
            try {{
                products = JSON.parse(savedProducts);
            }} catch(e) {{}}
        }}
        
        loadProducts();
        updateCartCount();
    </script>
</body>
</html>'''
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ تم إنشاء index.html")


def create_products_json(products):
    """حفظ المنتجات في ملف JSON"""
    data = {
        'products': products,
        'total': len(products),
        'last_update': datetime.now().isoformat(),
        'config': CONFIG
    }
    
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ تم حفظ {len(products)} منتج في products.json")
    
    # إنشاء API
    os.makedirs('api', exist_ok=True)
    with open('api/products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print("✅ تم إنشاء api/products.json")


def create_readme():
    """إنشاء ملف README.md"""
    readme = f'''# 🪒 {CONFIG['site_name']}

## متجر مستلزمات الحلاقة الاحترافية

### 🔗 روابط مهمة:
- **Cloudinary**: https://collection.cloudinary.com/{CONFIG['cloudinary_cloud']}/{CONFIG['cloudinary_folder']}
- **Firebase**: {CONFIG['firebase_url']}

### 🔑 معلومات الإدارة:
- **رمز الدخول**: `{CONFIG['admin_password']}`

### ✨ المميزات:
- إضافة منتجات جديدة مع الصور والأسعار
- سلة تسوق متكاملة
- طلب مباشر عبر Firebase
- تصميم متجاوب مع جميع الأجهزة
- تحديث تلقائي للمنتجات
- زر واتساب للتواصل المباشر

### 📞 التواصل:
- الهاتف: {CONFIG['phone']}
- واتساب: {CONFIG['whatsapp']}
'''
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    print("✅ تم إنشاء README.md")


def create_cname():
    """إنشاء ملف CNAME إذا وجد"""
    # اختياري - إذا كان لديك دومين مخصص
    pass


def main():
    """الدالة الرئيسية - تشغل كل شيء"""
    print("=" * 60)
    print("🪒 بدء إنشاء متجر الحلاقة SO2_MK")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # تحميل المنتجات
    products = load_products()
    
    # إنشاء الملفات
    print("\n📝 إنشاء الملفات...")
    print("-" * 40)
    
    create_index_html(products)
    create_products_json(products)
    create_readme()
    create_cname()
    
    print("-" * 40)
    print(f"✅ تم إنشاء جميع الملفات بنجاح!")
    print(f"📊 إجمالي المنتجات: {len(products)}")
    print(f"🔑 رمز الإدارة: {CONFIG['admin_password']}")
    print("=" * 60)
    print("🎉 الموقع جاهز للنشر!")
    print("=" * 60)


if __name__ == "__main__":
    main()
