#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🪒 متجر الحلاقة SO2_MK
Cloudinary: dmla61v7n/so2_mk
Firebase: gomrka-420d0
"""

import json
import os
from datetime import datetime

SITE_NAME = "صالون MK للحلاقة"
CLOUD_NAME = "dmla61v7n"
FOLDER = "so2_mk"
FIREBASE = "https://gomrka-420d0-default-rtdb.firebaseio.com"
ADMIN_PASS = "1234"
CURRENCY = "ريال"

def html():
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{SITE_NAME}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Cairo', sans-serif; background: #f0f2f5; }}
        .top-bar {{ background: #1a1a1a; color: #c9a96e; padding: 8px 0; font-size: 0.9rem; }}
        .navbar {{ background: linear-gradient(135deg, #1a1a1a, #2c2c2c); padding: 15px 0; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }}
        .navbar-brand {{ font-size: 1.8rem; font-weight: 900; color: #c9a96e !important; }}
        .navbar-brand i {{ animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.1); }} }}
        .nav-link {{ color: #fff !important; margin: 0 15px; font-weight: 600; }}
        .nav-link:hover {{ color: #c9a96e !important; }}
        .btn-cart {{ background: transparent; border: 2px solid #fff; color: #fff; padding: 10px 20px; border-radius: 50px; cursor: pointer; position: relative; }}
        .btn-cart:hover {{ background: #fff; color: #1a1a1a; }}
        .cart-count {{ position: absolute; top: -8px; right: -8px; background: #dc3545; color: white; width: 22px; height: 22px; border-radius: 50%; font-size: 0.75rem; display: flex; align-items: center; justify-content: center; font-weight: 700; }}
        
        .hero {{ background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1200'); background-size: cover; background-position: center; color: white; padding: 120px 0; text-align: center; }}
        .hero h1 {{ font-size: 3.5rem; font-weight: 900; }}
        .hero h1 span {{ color: #c9a96e; }}
        .btn-hero {{ background: #c9a96e; color: #1a1a1a; padding: 15px 40px; border-radius: 50px; font-size: 1.2rem; font-weight: 700; text-decoration: none; display: inline-block; }}
        
        .features {{ padding: 80px 0; background: white; }}
        .feature-box {{ text-align: center; padding: 40px 20px; border-radius: 20px; background: #fff; box-shadow: 0 5px 30px rgba(0,0,0,0.05); margin-bottom: 30px; }}
        .feature-box i {{ font-size: 3rem; color: #c9a96e; margin-bottom: 20px; }}
        .feature-box h4 {{ font-weight: 700; }}
        
        .products-section {{ padding: 80px 0; background: #f8f9fa; }}
        .section-title {{ text-align: center; margin-bottom: 60px; }}
        .section-title h2 {{ font-size: 2.5rem; font-weight: 900; color: #1a1a1a; display: inline-block; padding-bottom: 20px; position: relative; }}
        .section-title h2::after {{ content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 100px; height: 4px; background: #c9a96e; border-radius: 2px; }}
        
        .product-card {{ background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.08); transition: 0.4s; height: 100%; border: 2px solid transparent; }}
        .product-card:hover {{ transform: translateY(-15px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-color: #c9a96e; }}
        .product-img {{ position: relative; height: 280px; overflow: hidden; background: #f5f5f5; }}
        .product-img img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        .product-card:hover .product-img img {{ transform: scale(1.1); }}
        .product-badge {{ position: absolute; top: 15px; right: 15px; background: linear-gradient(135deg, #c9a96e, #b8963d); color: #1a1a1a; padding: 8px 18px; border-radius: 50px; font-size: 0.85rem; font-weight: 700; }}
        .product-info {{ padding: 25px; }}
        .product-price {{ font-size: 2rem; font-weight: 900; color: #c9a96e; margin: 15px 0; }}
        .qty-control {{ display: flex; align-items: center; gap: 10px; margin-bottom: 15px; }}
        .qty-btn {{ width: 35px; height: 35px; border-radius: 50%; border: 2px solid #c9a96e; background: white; color: #c9a96e; font-size: 1.2rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; }}
        .qty-btn:hover {{ background: #c9a96e; color: white; }}
        .qty-input {{ width: 50px; text-align: center; border: 2px solid #eee; border-radius: 10px; padding: 8px; font-weight: 700; }}
        .btn-add {{ background: linear-gradient(135deg, #1a1a1a, #333); color: #c9a96e; border: none; padding: 12px 30px; border-radius: 50px; font-weight: 700; cursor: pointer; width: 100%; }}
        .btn-add:hover {{ background: #c9a96e; color: #1a1a1a; }}
        
        .modal-overlay {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; align-items: center; justify-content: center; }}
        .modal-overlay.show {{ display: flex; }}
        .modal-box {{ background: white; border-radius: 20px; padding: 40px; width: 90%; max-width: 550px; max-height: 90vh; overflow-y: auto; position: relative; animation: modalIn 0.4s ease; }}
        @keyframes modalIn {{ from {{ transform: translateY(-50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }}
        .form-control {{ border: 2px solid #eee; border-radius: 12px; padding: 12px 15px; margin-bottom: 15px; width: 100%; font-family: 'Cairo', sans-serif; }}
        .form-control:focus {{ border-color: #c9a96e; outline: none; }}
        .btn-submit {{ background: linear-gradient(135deg, #c9a96e, #b8963d); color: #1a1a1a; border: none; padding: 14px 30px; border-radius: 50px; font-weight: 700; cursor: pointer; width: 100%; font-size: 1.1rem; }}
        .btn-close-modal {{ position: absolute; top: 15px; left: 15px; background: #f5f5f5; border: none; width: 35px; height: 35px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; }}
        .btn-close-modal:hover {{ background: #dc3545; color: white; }}
        
        .upload-area {{ border: 3px dashed #c9a96e; border-radius: 15px; padding: 30px; text-align: center; cursor: pointer; margin-bottom: 15px; background: #fafafa; }}
        .upload-area:hover {{ background: #f0f0f0; }}
        .upload-area i {{ font-size: 3rem; color: #c9a96e; margin-bottom: 10px; }}
        .upload-area img {{ max-width: 100%; max-height: 200px; border-radius: 10px; margin-top: 10px; }}
        .progress {{ height: 20px; background: #e9ecef; border-radius: 10px; overflow: hidden; margin-top: 10px; }}
        .progress-bar {{ height: 100%; background: #c9a96e; transition: width 0.3s; display: flex; align-items: center; justify-content: center; color: #1a1a1a; font-weight: 700; }}
        
        .toast {{ position: fixed; top: 20px; left: 50%; transform: translateX(-50%); padding: 15px 30px; border-radius: 50px; color: white; font-weight: 700; z-index: 99999; display: none; }}
        .cart-modal .modal-content {{ border-radius: 20px; border: none; }}
        .cart-modal .modal-header {{ background: #1a1a1a; color: #c9a96e; border-radius: 20px 20px 0 0; }}
        
        .whatsapp-btn {{ position: fixed; bottom: 30px; left: 30px; background: #25d366; color: white; width: 65px; height: 65px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px; box-shadow: 0 8px 30px rgba(37,211,102,0.4); z-index: 1000; text-decoration: none; animation: bounce 2s infinite; }}
        @keyframes bounce {{ 0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }} 40% {{ transform: translateY(-20px); }} 60% {{ transform: translateY(-10px); }} }}
        
        .upload-float-btn {{ position: fixed; bottom: 30px; right: 30px; background: linear-gradient(135deg, #c9a96e, #b8963d); color: #1a1a1a; width: 65px; height: 65px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; box-shadow: 0 8px 30px rgba(201,169,110,0.5); z-index: 1000; cursor: pointer; border: none; animation: bounce 2s infinite; }}
        .upload-float-btn:hover {{ animation: none; transform: scale(1.1); }}
        .upload-float-btn::after {{ content: 'تحميل منتج'; position: absolute; right: 75px; background: #1a1a1a; color: #c9a96e; padding: 8px 15px; border-radius: 25px; font-size: 0.85rem; font-weight: 700; white-space: nowrap; opacity: 0; transition: 0.3s; }}
        .upload-float-btn:hover::after {{ opacity: 1; }}
        
        footer {{ background: #1a1a1a; color: white; padding: 50px 0 30px; }}
        footer h5 {{ color: #c9a96e; font-weight: 700; }}
        .lock-icon {{ font-size: 5rem; color: #c9a96e; display: block; margin-bottom: 20px; }}
        @media (max-width: 768px) {{ .hero h1 {{ font-size: 2rem; }} .product-img {{ height: 200px; }} }}
    </style>
</head>
<body>
    <div class="top-bar"><div class="container text-center">🚚 توصيل مجاني للطلبات فوق 200 {CURRENCY} | 📞 0500000000</div></div>

    <nav class="navbar navbar-expand-lg sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="fas fa-cut"></i> {SITE_NAME}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="nav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="#home">الرئيسية</a></li>
                    <li class="nav-item"><a class="nav-link" href="#products">المنتجات</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">اتصل بنا</a></li>
                </ul>
                <button class="btn-cart" data-bs-toggle="modal" data-bs-target="#cartModal"><i class="fas fa-shopping-cart"></i><span class="cart-count" id="cartCount">0</span></button>
            </div>
        </div>
    </nav>

    <header class="hero" id="home">
        <div class="container"><h1>أهلاً بك في <span>{SITE_NAME}</span></h1><p>أفضل مستلزمات الحلاقة الاحترافية</p><a href="#products" class="btn-hero"><i class="fas fa-shopping-bag"></i> تصفح المنتجات</a></div>
    </header>

    <section class="features"><div class="container"><div class="section-title"><h2>لماذا تختارنا؟</h2></div><div class="row">
        <div class="col-md-4"><div class="feature-box"><i class="fas fa-truck-fast"></i><h4>توصيل سريع</h4></div></div>
        <div class="col-md-4"><div class="feature-box"><i class="fas fa-medal"></i><h4>منتجات أصلية</h4></div></div>
        <div class="col-md-4"><div class="feature-box"><i class="fas fa-headset"></i><h4>دعم فني</h4></div></div>
    </div></div></section>

    <section class="products-section" id="products"><div class="container"><div class="section-title"><h2>🪒 منتجاتنا</h2></div><div class="row" id="productsGrid"></div></div></section>

    <section id="contact" style="padding:80px 0;background:white;"><div class="container"><div class="section-title"><h2>اطلب الآن</h2></div><div class="row justify-content-center"><div class="col-md-8">
        <form id="orderForm">
            <div class="row"><div class="col-md-6 mb-3"><input type="text" class="form-control" id="name" placeholder="الاسم الكامل *" required></div><div class="col-md-6 mb-3"><input type="tel" class="form-control" id="phone" placeholder="رقم الهاتف *" required></div></div>
            <div class="mb-3"><textarea class="form-control" id="details" rows="4" placeholder="تفاصيل الطلب"></textarea></div>
            <button type="submit" class="btn-submit"><i class="fas fa-paper-plane"></i> إرسال الطلب</button>
        </form>
    </div></div></div></section>

    <!-- نافذة تحميل المنتج -->
    <div class="modal-overlay" id="uploadModal">
        <div class="modal-box">
            <button class="btn-close-modal" onclick="closeUploadModal()">✕</button>
            <div id="passwordStep">
                <div style="text-align:center;"><i class="fas fa-lock lock-icon"></i><h3>🔐 تحميل منتج جديد</h3><p style="color:#666;">أدخل رمز التحقق للمتابعة</p></div>
                <input type="password" id="uploadPassword" class="form-control" placeholder="🔑 أدخل الرمز السري">
                <button class="btn-submit mt-3" onclick="verifyUploadPassword()"><i class="fas fa-check"></i> تحقق واستمر</button>
            </div>
            <div id="uploadStep" style="display:none;">
                <div style="text-align:center;margin-bottom:25px;"><i class="fas fa-cloud-upload-alt" style="font-size:3rem;color:#c9a96e;"></i><h3>📤 رفع منتج جديد</h3><p style="color:#666;">ارفع صورة المنتج وأدخل بياناته</p></div>
                <form id="uploadForm">
                    <label style="font-weight:700;display:block;">📝 اسم المنتج *</label>
                    <input type="text" id="prodName" class="form-control" placeholder="اسم المنتج" required>
                    <label style="font-weight:700;display:block;">💰 السعر الذي تحدده ({CURRENCY}) *</label>
                    <input type="number" id="prodPrice" class="form-control" placeholder="أدخل السعر" required>
                    <label style="font-weight:700;display:block;">📂 الفئة</label>
                    <select id="prodCat" class="form-control"><option value="">اختر الفئة</option><option>ماكينات حلاقة</option><option>أمشاط</option><option>كريمات حلاقة</option><option>فوط</option><option>زيوت</option><option>فرش</option><option>معقمات</option><option>إكسسوارات</option></select>
                    
                    <label style="font-weight:700;display:block;">🖼️ رفع صورة المنتج *</label>
                    <div class="upload-area" id="uploadArea" onclick="document.getElementById('fileInput').click()">
                        <i class="fas fa-cloud-upload-alt"></i>
                        <p><strong>اضغط هنا لرفع صورة المنتج</strong></p>
                        <small style="color:#999;">ترفع إلى: {CLOUD_NAME}/{FOLDER}</small>
                        <img id="imagePreview" style="display:none;">
                        <div id="uploadProgress" style="display:none;"></div>
                    </div>
                    <input type="file" id="fileInput" accept="image/*" style="display:none;" onchange="uploadImageToCloudinary()">
                    <input type="hidden" id="prodImage" required>
                    
                    <label style="font-weight:700;display:block;">📝 وصف المنتج</label>
                    <textarea id="prodDesc" class="form-control" rows="2" placeholder="وصف مختصر"></textarea>
                    <label style="font-weight:700;display:block;">📦 المخزون</label>
                    <input type="number" id="prodStock" class="form-control" value="100" min="1">
                    <button type="submit" class="btn-submit mt-4"><i class="fas fa-check-circle"></i> رفع المنتج الآن</button>
                </form>
            </div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <div class="modal fade cart-modal" id="cartModal">
        <div class="modal-dialog modal-lg"><div class="modal-content">
            <div class="modal-header"><h5 class="modal-title">🛒 سلة التسوق</h5><button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button></div>
            <div class="modal-body" id="cartBody"><p class="text-center text-muted py-4">السلة فارغة</p></div>
            <div class="modal-footer"><button class="btn-submit" onclick="checkout()">إتمام الطلب</button></div>
        </div></div>
    </div>

    <a href="https://wa.me/966500000000" class="whatsapp-btn" target="_blank"><i class="fab fa-whatsapp"></i></a>
    <button class="upload-float-btn" onclick="openUploadModal()" title="تحميل منتج"><i class="fas fa-cloud-upload-alt"></i></button>

    <footer><div class="container"><div class="row">
        <div class="col-md-4 mb-4"><h5><i class="fas fa-cut"></i> {SITE_NAME}</h5></div>
        <div class="col-md-4 mb-4"><h5>روابط سريعة</h5><a href="#home" class="text-white d-block mb-2">الرئيسية</a></div>
        <div class="col-md-4 mb-4"><h5>تواصل معنا</h5><p><i class="fas fa-phone"></i> 0500000000</p></div>
    </div><hr style="border-color:#333;"><p class="text-center mb-0">&copy; 2024 {SITE_NAME}</p></div></footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.0/firebase-database-compat.js"></script>
    <script>
        firebase.initializeApp({{ databaseURL: "{FIREBASE}" }});
        const db = firebase.database();
        let products = [], cart = [];
        const ADMIN_PASS = "{ADMIN_PASS}";
        const CLOUD_NAME = "{CLOUD_NAME}";
        const UPLOAD_FOLDER = "{FOLDER}";
        
        async function loadProducts() {{
            try {{ const snap = await db.ref('products').once('value'); products = snap.val() ? Object.values(snap.val()) : []; }} catch(e) {{}}
            if (!products.length) {{ const saved = localStorage.getItem('mk_products'); products = saved ? JSON.parse(saved) : []; }}
            renderProducts();
        }}
        
        function renderProducts() {{
            const grid = document.getElementById('productsGrid');
            if (!products.length) {{ grid.innerHTML = '<div class="col-12 text-center py-5"><i class="fas fa-box-open" style="font-size:4rem;color:#ccc;"></i><h4>لا توجد منتجات</h4><p>اضغط زر التحميل <i class="fas fa-cloud-upload-alt"></i> لإضافة منتج</p></div>'; return; }}
            grid.innerHTML = products.map(p => {{
                const stars = '⭐'.repeat(Math.floor(p.rating || 5));
                return `<div class="col-md-4 col-lg-3 mb-4"><div class="product-card"><div class="product-img"><img src="${{p.image}}" alt="${{p.name}}" onerror="this.src='https://placehold.co/400x300/1a1a1a/c9a96e?text=Error'"><span class="product-badge">${{p.category || 'منتج'}}</span></div><div class="product-info"><h5>${{p.name}}</h5><div style="color:#ffc107;">${{stars}} (${{p.rating || 5}})</div><div class="product-price">${{p.price}} {CURRENCY}</div><p class="product-stock" style="color:#28a745;">📦 ${{p.stock || 0}}</p><div class="qty-control"><button class="qty-btn" onclick="changeQty(${{p.id}},-1)">−</button><input type="number" id="qty-${{p.id}}" class="qty-input" value="1" min="1" max="${{p.stock || 10}}" readonly><button class="qty-btn" onclick="changeQty(${{p.id}},1)">+</button></div><button class="btn-add" onclick="addToCart(${{p.id}})"><i class="fas fa-cart-plus"></i> أضف للسلة</button></div></div></div>`;
            }}).join('');
        }}
        
        function changeQty(id,d) {{ const inp=document.getElementById('qty-'+id); let v=parseInt(inp.value)+d; const p=products.find(x=>x.id===id); const max=p?(p.stock||10):10; if(v<1)v=1; if(v>max)v=max; inp.value=v; }}
        
        function addToCart(id) {{ const p=products.find(x=>x.id===id); if(!p)return; const qty=parseInt(document.getElementById('qty-'+id).value); const exist=cart.find(x=>x.id===id); if(exist) exist.quantity+=qty; else cart.push({{id:p.id,name:p.name,price:p.price,image:p.image,quantity:qty}}); updateCart(); showToast('✅ تمت الإضافة!','success'); }}
        function updateCart() {{ document.getElementById('cartCount').textContent = cart.reduce((s,i)=>s+i.quantity,0); }}
        
        function showCart() {{
            const body=document.getElementById('cartBody');
            if(!cart.length) {{ body.innerHTML='<p class="text-center text-muted py-4">السلة فارغة</p>'; return; }}
            let total=0; body.innerHTML = cart.map((item,i)=>{{ const st=item.price*item.quantity; total+=st; return `<div class="d-flex justify-content-between mb-3 p-3 border rounded"><div><h6>${{item.name}}</h6><small>${{item.quantity}}×${{item.price}}=${{st}} {CURRENCY}</small></div><button class="btn btn-sm btn-danger" onclick="removeCart(${{i}})"><i class="fas fa-trash"></i></button></div>`; }}).join('') + `<div class="text-end mt-3"><h5>المجموع: <span style="color:#c9a96e;">${{total}} {CURRENCY}</span></h5></div>`;
        }}
        function removeCart(i){{ cart.splice(i,1); updateCart(); showCart(); }}
        
        function checkout() {{ if(!cart.length){{ showToast('⚠️ السلة فارغة!','error'); return; }} document.getElementById('details').value=cart.map(i=>`${{i.name}} (${{i.quantity}}×)`).join('\\n'); bootstrap.Modal.getInstance(document.getElementById('cartModal')).hide(); document.getElementById('contact').scrollIntoView({{behavior:'smooth'}}); }}
        
        function openUploadModal() {{ document.getElementById('uploadModal').classList.add('show'); document.getElementById('passwordStep').style.display='block'; document.getElementById('uploadStep').style.display='none'; document.getElementById('uploadPassword').value=''; document.getElementById('uploadForm').reset(); document.getElementById('imagePreview').style.display='none'; document.getElementById('uploadProgress').style.display='none'; }}
        function closeUploadModal() {{ document.getElementById('uploadModal').classList.remove('show'); }}
        function verifyUploadPassword() {{ if(document.getElementById('uploadPassword').value===ADMIN_PASS){{ document.getElementById('passwordStep').style.display='none'; document.getElementById('uploadStep').style.display='block'; showToast('✅ تم التحقق!','success'); }} else {{ showToast('❌ رمز خاطئ!','error'); }} }}
        
        // ✅ رفع الصورة إلى Cloudinary مع الإعدادات الصحيحة
        function uploadImageToCloudinary() {{
            const file = document.getElementById('fileInput').files[0];
            if (!file) return;
            
            const progressDiv = document.getElementById('uploadProgress');
            progressDiv.style.display = 'block';
            progressDiv.innerHTML = '<div class="progress"><div class="progress-bar" style="width:10%">جاري الرفع...</div></div>';
            
            const formData = new FormData();
            formData.append('file', file);
            formData.append('upload_preset', 'so2_mk_preset');
            formData.append('folder', UPLOAD_FOLDER);
            formData.append('cloud_name', CLOUD_NAME);
            
            const xhr = new XMLHttpRequest();
            xhr.open('POST', 'https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', true);
            
            xhr.upload.onprogress = function(e) {{
                if (e.lengthComputable) {{
                    const percent = Math.round((e.loaded / e.total) * 100);
                    progressDiv.innerHTML = '<div class="progress"><div class="progress-bar" style="width:' + percent + '%">' + percent + '%</div></div>';
                }}
            }};
            
            xhr.onload = function() {{
                progressDiv.style.display = 'none';
                if (xhr.status === 200) {{
                    const response = JSON.parse(xhr.responseText);
                    document.getElementById('prodImage').value = response.secure_url;
                    const preview = document.getElementById('imagePreview');
                    preview.src = response.secure_url;
                    preview.style.display = 'block';
                    showToast('✅ تم رفع الصورة بنجاح إلى Cloudinary!', 'success');
                }} else {{
                    // لو فشل الـ preset الأول، نجرب preset تاني
                    tryUploadWithDifferentPreset(file);
                }}
            }};
            
            xhr.onerror = function() {{
                progressDiv.style.display = 'none';
                showToast('❌ خطأ في الاتصال - تأكد من Upload Preset في Cloudinary', 'error');
            }};
            
            xhr.send(formData);
        }}
        
        // ✅ تجربة Preset مختلف إذا فشل الأول
        function tryUploadWithDifferentPreset(file) {{
            const progressDiv = document.getElementById('uploadProgress');
            progressDiv.style.display = 'block';
            progressDiv.innerHTML = '<div class="progress"><div class="progress-bar" style="width:30%">محاولة بديلة...</div></div>';
            
            const presets = ['ml_default', 'unsigned_upload', 'default', 'so2_mk'];
            let currentIndex = 0;
            
            function tryNext() {{
                if (currentIndex >= presets.length) {{
                    progressDiv.style.display = 'none';
                    showToast('❌ فشل الرفع - تأكد من وجود Upload Preset في إعدادات Cloudinary', 'error');
                    return;
                }}
                
                const formData = new FormData();
                formData.append('file', file);
                formData.append('upload_preset', presets[currentIndex]);
                formData.append('folder', UPLOAD_FOLDER);
                
                const xhr = new XMLHttpRequest();
                xhr.open('POST', 'https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', true);
                
                xhr.onload = function() {{
                    if (xhr.status === 200) {{
                        const response = JSON.parse(xhr.responseText);
                        document.getElementById('prodImage').value = response.secure_url;
                        const preview = document.getElementById('imagePreview');
                        preview.src = response.secure_url;
                        preview.style.display = 'block';
                        progressDiv.style.display = 'none';
                        showToast('✅ تم رفع الصورة! (preset: ' + presets[currentIndex] + ')', 'success');
                    }} else {{
                        currentIndex++;
                        tryNext();
                    }}
                }};
                
                xhr.onerror = function() {{ currentIndex++; tryNext(); }};
                xhr.send(formData);
            }}
            
            tryNext();
        }}
        
        document.getElementById('uploadForm').addEventListener('submit', async function(e) {{
            e.preventDefault();
            const imgUrl = document.getElementById('prodImage').value;
            if (!imgUrl) {{ showToast('⚠️ ارفع صورة المنتج أولاً!','error'); return; }}
            const product = {{ id: Date.now(), name: document.getElementById('prodName').value, price: parseInt(document.getElementById('prodPrice').value), category: document.getElementById('prodCat').value||'منتج', image: imgUrl, description: document.getElementById('prodDesc').value, stock: parseInt(document.getElementById('prodStock').value)||100, rating: 5, created: new Date().toISOString() }};
            products.push(product); localStorage.setItem('mk_products', JSON.stringify(products));
            try {{ await db.ref('products/'+product.id).set(product); }} catch(e) {{}}
            renderProducts(); closeUploadModal(); showToast('✅ تم رفع المنتج! 🎉','success');
            this.reset(); document.getElementById('imagePreview').style.display='none';
        }});
        
        document.getElementById('orderForm').addEventListener('submit', async function(e) {{
            e.preventDefault(); if(!cart.length){{ showToast('⚠️ السلة فارغة!','error'); return; }}
            const order = {{ name: document.getElementById('name').value, phone: document.getElementById('phone').value, details: document.getElementById('details').value, cart: cart, total: cart.reduce((s,i)=>s+(i.price*i.quantity),0), time: firebase.database.ServerValue.TIMESTAMP, status: 'جديد' }};
            try {{ await db.ref('orders').push(order); showToast('✅ تم إرسال الطلب!','success'); this.reset(); cart=[]; updateCart(); showCart(); }} catch(e) {{ showToast('❌ خطأ','error'); }}
        }});
        
        function showToast(msg,type) {{ const t=document.getElementById('toast'); t.textContent=msg; t.style.background=type==='error'?'#dc3545':'#28a965'; t.style.display='block'; setTimeout(()=>t.style.display='none',3000); }}
        
        document.getElementById('cartModal').addEventListener('show.bs.modal', showCart);
        document.getElementById('uploadModal').addEventListener('click', function(e){{ if(e.target===this) closeUploadModal(); }});
        loadProducts(); updateCart();
    </script>
</body>
</html>'''

def main():
    print("🪒 SO2_MK - متجر الحلاقة")
    with open('index.html', 'w', encoding='utf-8') as f: f.write(html())
    print("✅ index.html")
    with open('products.json', 'w', encoding='utf-8') as f: json.dump({{'products': [], 'total': 0, 'last_update': datetime.now().isoformat()}}, f)
    os.makedirs('api', exist_ok=True)
    with open('api/products.json', 'w', encoding='utf-8') as f: json.dump([], f)
    with open('README.md', 'w', encoding='utf-8') as f: f.write(f'# 🪒 {SITE_NAME}\n## Cloudinary: {CLOUD_NAME}/{FOLDER}\n## رمز: {ADMIN_PASS}')
    print(f"🎉 تم! Cloudinary: {CLOUD_NAME}/{FOLDER}")

if __name__ == '__main__':
    main()
